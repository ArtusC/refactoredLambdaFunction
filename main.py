import pandas as pd
import requests
import json
import re
import pymysql
import numpy as np
from unicaps import CaptchaSolver, CaptchaSolvingService
import os
import logging

import static
import helper
import headers_and_params as hp


# gets lbct vessel data as a pandas dataframe
def get_lbct_vessel():
    try:
        response = requests.get(static.LBCT_URL, verify=False)
        response = json.loads(response.text)
        response_keys = response[0].keys()

        df = pd.DataFrame([x.values() for x in response], columns=response_keys)

        df["terminal"] = "LBCT"
        df = df[static.LBCT_COLUMN_VALUES]
        df.columns = static.LBCT_COLUMN_DF

        df['eta'] = df['eta'].apply(lambda x: helper.parse_date_to_month_day_year(
            x, static.PARSE_DATE_FORMAT_LBCT))
        df['etd'] = df['etd'].apply(lambda x: helper.parse_date_to_month_day_year(
            x, static.PARSE_DATE_FORMAT_LBCT))

        return df
    
    except:
        return None


# gets piera vessel data as a pandas dataframe
def get_piera_vessel():
    try:
        cookies = login_piera()
        headers = hp.PIERA_HEADERS
        params = hp.PIERA_PARAMS

        response = requests.get(static.PIERA_URL, params=params,
                                cookies=cookies, headers=headers)

        df = pd.read_html(response.text)
        df[0]["terminal"] = "PIERA"
        df = df[0][static.PIERA_COLUMN_VALUES]
        df.columns = static.PIERA_COLUMN_DF

        df['eta'] = df['eta'].apply(lambda x: helper.parse_date_to_month_day_year(
            x, static.PARSE_DATE_FORMAT_PIERA))
        df['etd'] = df['etd'].apply(lambda x: helper.parse_date_to_month_day_year(
            x, static.PARSE_DATE_FORMAT_PIERA))

        return df

    except:
        return None


# gets Fenix Marine vessel data as a pandas dataframe
def get_fenix_vessel():
    cookies = hp.FENIX_COOKIES
    headers = hp.FENIX_HEADERS
    params = hp.FENIX_PARAMS

    try:
        response = requests.get(
            static.FENIX_URL,
            params=params,
            cookies=cookies,
            headers=headers,
            verify=False
        )
        df = pd.read_html(response.text)[0][6:].drop("Unnamed: 0", axis=1)
        df.columns = static.FENIX_COLUMN_DF
        df["terminal"] = "Fenix"
        df = df[static.FENIX_COLUMN_VALUES]

        df['eta'] = df['eta'].apply(helper.format_date_fenix)
        df['etd'] = df['etd'].apply(helper.format_date_fenix)

        return df

    except:
        return None


# gets pct vessel data as a pandas dataframe
def get_pct_vessel():
    try: 
        cookies = login_pct()
        headers = hp.PCT_HEADERS
        params = hp.PCT_PARAMS

        response = requests.get(static.PCT_URL, params=params,
                                cookies=cookies, headers=headers)
        df = pd.read_html(response.text)[0]
        df['terminal'] = "PCT"
        df = df[static.PCT_COLUMN_VALUES]
        df.columns = static.PCT_COLUMN_DF

        df['eta'] = df['eta'].apply(
            lambda x: helper.parse_date_to_month_day_year(x, static.PARSE_DATE_FORMAT_PCT))
        df['etd'] = df['etd'].apply(
            lambda x: helper.parse_date_to_month_day_year(x, static.PARSE_DATE_FORMAT_PCT))

        return df

    except:
        return None


# gets its vessel data as a pandas dataframe
def get_its_vessel():
    try:
        cookies_from_db = get_cookie("ITS")
        cookies = json.loads(cookies_from_db)
        headers = hp.ITS_HEADERS

        response = requests.request(
            "POST", static.ITS_URL, headers=headers, cookies=cookies)
        if 'Log in' in response.text:
            cookies = login_its()
            response = requests.request(
                "GET", static.ITS_URL, headers=headers, cookies=cookies)
        df = pd.read_html(response.text)[0][::2]
        df["terminal"] = "ITS"
        df = df[static.ITS_COLUMN_VALUES]
        df.columns = static.ITS_COLUMN_DF

        df['eta'] = df['eta'].apply(lambda x: helper.parse_date_to_month_day_year(x, static.PARSE_DATE_FORMAT_ITS))
        df['etd'] = df['etd'].apply(lambda x: helper.parse_date_to_month_day_year(x, static.PARSE_DATE_FORMAT_ITS))

        return df

    except:
        return None


# gets ets vessel data as a pandas dataframe
def get_ets_vessel():
    cookies = hp.ETS_COOKIES
    headers = hp.ETS_HEADERS
    try:
        response = requests.get(static.ETS_URL, cookies=cookies,
                                headers=headers, verify=False)

        df = pd.read_html(response.text)[1]
        df.columns = df.iloc[0].values
        df["terminal"] = 'ETS'
        df = df[static.ETS_COLUMN_VALUES][1:]
        for num in range(len(df)):
            df.iloc[num, 2] = df.iloc[num, 2].split()[0][:-4] + \
                df.iloc[num, 2].split()[0][-2:]
            df.iloc[num, 3] = df.iloc[num, 3].split()[0][:-4] + \
                df.iloc[num, 3].split()[0][-2:]
        df.columns = static.ETS_COLUMN_DF

        return df

    except:
        return None


# gets apm vessel data as a pandas dataframe
def get_apm_vessel():
    try:
        s = requests.Session()
        headers = hp.APM_FIRST_HEADERS
        s.proxies = hp.PROXY_CONNECTIONS
        response = s.get(static.APM_FIRST_URL,
                        headers=headers, timeout=5, verify=False)
        
        cookies = response.headers.get('Set-Cookie')
        correced_apm_headers = hp.APM_SECOND_HEADERS.copy()
        correced_apm_headers['cookies'] = cookies
        params = hp.APM_PARAMS
        response = requests.get(
            static.APM_SECOND_URL,
            params=params,
            headers=correced_apm_headers,
            verify=False
        )
        df = pd.DataFrame([response.json()['Results'][y][x] for x in range(len(response.json()['Results'][0])) for y in
                        range(len(response.json()['Results']))])
        df = pd.DataFrame(
            [[df.iloc[x].ShipName['Value'], df.iloc[x].ArrivalTime['Value'].split()[0], df.iloc[x].DepartureTime['Value'].split()[0] if df.iloc[x].DepartureTime['Value'] else ""] for x in
            range(len(df))], columns=static.APM_COLUMN_DF)
        
        df["terminal"] = "APM"
        df = df[static.APM_COLUMN_VALUES]
        
        return df

    except:
        return None


# gets yti vessel data as a pandas dataframe
def get_yti_vessel():
    
    headers = hp.YTI_HEADERS
    params = hp.YTI_PARAMS

    try: 
        response = requests.get(
            static.YTI_URL,
            params=params,
            headers=headers,
            verify=False
        )
        df = pd.read_html(response.text)[0]
        df.columns = df.iloc[2]
        df["Terminal"] = "YTI"
        df.columns.name = ''
        df = df[static.YTI_COLUMN_VALUES][4:-5]
        df.columns = static.YTI_COLUMN_DF
        current_year = helper.current_year()

        df['eta'] = df['eta'].apply(lambda x: helper.parse_date_to_month_day_year(f'{x}/{current_year}', static.PARSE_DATE_FORMAT_YTI))
        df['etd'] = df['etd'].apply(lambda x: helper.parse_date_to_month_day_year(f'{x}/{current_year}', static.PARSE_DATE_FORMAT_YTI) if x != 'TBA' else x)
        
        return df

    except:
        return None


# gets wbct vessel data as a pandas dataframe
def get_wbct_vessel():
    headers = hp.WBCT_HEADERS
    params = hp.WBCT_PARAMS
    
    try:
        response = requests.get(static.WBCT_URL, params=params, headers=headers)
        
        df = pd.read_html(response.text)[4]
        df.columns = df.iloc[0]
        df.columns.name = ''
        df["terminal"] = "WBCT"
        df = df[static.WBCT_COLUMN_VALUES][1:]
        df.columns = static.WBCT_COLUMN_DF
        
        return df

    except:
        return None


# gets trapac vessel data as a pandas dataframe
def get_trapac_vessel():
    myhtml = ""

    try:
        for _ in range(10):
            CAPTCHA_SOLVING_SERVICE = CaptchaSolvingService.ANTI_CAPTCHA
            captcha_solving_service_key = static.CAPTCHA_SOLVING_SERVICE_KEY

            # headers for the request
            headers = static.TRAPAC_HEADERS

            # init captcha solver and solve the captcha
            solver = CaptchaSolver(CAPTCHA_SOLVING_SERVICE,
                                captcha_solving_service_key)
            
            solved = solver.solve_recaptcha_v3(
                site_key=static.TRAPAC_CAPTCHA_SITE_KEY,
                page_url=static.TRAPAC_CAPTCHA_URL,
                action='quick_check',
                min_score=0.7
            )
            
            # prepare the payload data
            payload = hp.TRAPAC_PAYLOADS.copy()
            payload['recaptcha-token'] = solved.solution.token
            formated_dates = helper.format_date_trapac()
            payload.update(formated_dates)
            
            # make a request
            response = requests.post(
                static.TRAPAC_URL,
                data=payload,
                headers=headers
            )
            # check if response OK and parse the JSON contents
            response.raise_for_status()
            json_data = response.json()

            # check the result code
            result_code = json_data['code']

            if result_code == '200':
                myhtml = json_data['html']
                break
            elif result_code == 'recaptcha_v2':
                # Report bad captcha to the service (they should issue a refund)
                solved.report_bad()
            else:
                print(f'Unknown result code: {result_code}')

        if not myhtml:
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            logger.error('Without correct captcha solution')
            return None
        
        df = pd.read_html(myhtml)
        df = pd.DataFrame([df[0].iloc[x].values for x in range(0, len(df[0]), 2)][:-1], columns=static.TRAPAC_CULUMN_DF_RESPONSE)
        df["Terminal"] = "Trapac"
        df = df[static.TRAPAC_COLUMN_VALUES]
        df.columns = static.TRAPAC_COLUMN_DF

        df['eta'] = df['eta'].apply(lambda x: helper.parse_date_to_month_day_year(x, static.PARSE_DATE_FORMAT_TRAPAC))
        df['etd'] = df['etd'].apply(lambda x: helper.parse_date_to_month_day_year(x, static.PARSE_DATE_FORMAT_TRAPAC))

        return df

    except:
        return None

# gets tti vessel data as a pandas dataframe
def get_tti_vessel():
    try:
        headers = hp.TTI_HEADERS
        today, next_month = helper.format_date_tti()

        response = requests.get(static.TTI_FIRST_REQUEST, headers=headers, verify=False)
        cookies = dict(response.cookies)

        resp = requests.get(
            static.TTI_SECOND_REQUEST.format(today, next_month),
            cookies=cookies,
            headers=headers, verify=False)
        start_value, finish_value = resp.text.find('result = '), resp.text.find(';\r\n</script>')
        df = pd.DataFrame(json.loads(resp.text[start_value + 9:finish_value]))
        df["Terminal"] = "TTI"
        df = df[static.TTI_COLUMN_VALUES].dropna()
        df.columns = static.TTI_COLUMN_DF

        df['eta'] = df['eta'].apply(lambda x: helper.parse_date_to_month_day_year(x.replace("-", "/"), static.PARSE_DATE_FORMAT_TTI))
        df['etd'] = df['etd'].apply(lambda x: helper.parse_date_to_month_day_year(x.replace("-", "/"), static.PARSE_DATE_FORMAT_TTI))

        return df

    except:
        return None


def update_cookie(cookie, terminal):
    db = connect_to_database()
    mycursor = db.cursor()
    sql = "UPDATE Cookies SET Cookie=%s WHERE Terminal=%s"
    val = (cookie, terminal)
    result = mycursor.execute(sql, val)
    db.commit()
    db.close()


# gets a terminals cookie from the cookie table
def get_cookie(terminal):
    db = connect_to_database()
    mycursor = db.cursor()
    sql = "SELECT cookie from cookies WHERE Terminal=%s"
    mycursor.execute(sql, terminal)
    cookie = mycursor.fetchone()[0]
    db.close()
    return cookie


# zips two lists together
def ziplist(lst1, lst2):
    return np.array([[i, j] for i, j in zip(lst1, lst2)]).ravel()


# shifts the elements in a list l num spaces
def shiftlist(num, l):
    for x in range(num):
        l = l[-2:] + l[:-2]
    return l


def connect_to_database():
    return pymysql.connect(
        host=os.environ.get('host'),
        user=os.environ.get('user'),
        password=os.environ.get('password'),
        db=os.environ.get('db'),
        port=3306
    )

# automatically logs into piera
def login_piera():
    s = requests.Session()
    headers = hp.PIERA_LOGIN_FIRST_REQUEST_HEADERS
    response = s.get(static.PIERA_LOGIN_FIRST_URL,
                     headers=headers, verify=False, allow_redirects=True)

    cookies = dict(s.cookies)
    headers = hp.PIERA_LOGIN_SECOND_REQUEST_HEADERS
    params = hp.PIERA_LOGIN_SECOND_REQUEST_PARAM
    s = requests.Session()
    response = s.get(
        static.PIERA_LOGIN_SECOND_URL,
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )

    response = s.get(static.PIERA_LOGIN_FIRST_URL,
                     headers=headers, verify=False, allow_redirects=True)

    cookies = dict(s.cookies)
    headers = hp.PIERA_LOGIN_THIRD_REQUEST_HEADERS
    data = hp.PIERA_LOGIN_THIRD_REQUEST_PARAM
    response = s.post(
        static.PIERA_LOGIN_THIRD_URL,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    cookies = dict(s.cookies)
    return cookies


# automatically logs into Pct
def login_pct():
    s = requests.Session()
    headers = hp.PCT_LOGIN_FIRST_REQUEST_HEADERS
    response = s.get(static.PCT_LOGIN_FIRST_URL, headers=headers, verify=False)

    cookies = dict(s.cookies)
    headers = hp.PCT_LOGIN_SECOND_REQUEST_HEADERS
    data = hp.PCT_LOGIN_SECOND_REQUEST_PARAM
    response = s.post(
        static.PCT_LOGIN_SECOND_URL,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    cookies = dict(s.cookies)
    return cookies


def login_its():
    s = requests.Session()
    headers = hp.ITS_LOGIN_FIRST_HEADERS
    response = s.get(static.ITS_LOGIN_FIRST_URL, headers=headers, verify=False)
    cookies = dict(response.cookies)
    
    token_pattern = r'<input name="__RequestVerificationToken" type="hidden" value=(.*?) \/>'
    token = re.search(token_pattern, response.text).group(1).replace('"', "")

    headers = hp.ITS_LOGIN_HEADERS

    data = hp.ITS_LOGIN_PARAMS.copy()
    data['__RequestVerificationToken'] = token

    response = s.post(static.ITS_LOGIN_SECOND_URL, cookies=cookies, headers=headers, data=data, allow_redirects=True)
    cookies = dict(s.cookies)
    return cookies


def get_vessel_master():
    vessel_master = pd.concat([get_apm_vessel(), get_ets_vessel(), get_fenix_vessel(), get_its_vessel(),
                               get_lbct_vessel(), get_pct_vessel(), get_piera_vessel(), get_trapac_vessel(),
                               get_tti_vessel(), get_wbct_vessel(), get_yti_vessel()])
    return vessel_master


def set_vessel_schedules():
    vessel_master = get_vessel_master()
    db = connect_to_database()
    cursor = db.cursor()
    table_name = "a2z.vessels"
    # Add last_updated to the list of columns
    columns = static.VESSEL_MASTER_COLUMN_DF

    # Get the values for all rows and replace NaN values with None
    values = [tuple(row) if not any(pd.isna(row)) else tuple(None for _ in range(len(row))) for row in
              vessel_master[static.VESSEL_MASTER_COLUMN_VALUES].values]

    # Create the SQL query string with 'INSERT IGNORE' clause
    query = f"INSERT IGNORE INTO {table_name} ({','.join(columns)}) VALUES (%s,%s,%s,%s,NOW()) ON DUPLICATE KEY UPDATE terminal = VALUES(terminal), last_updated = NOW();"

    # Execute the query with all values using executemany
    cursor.executemany(query, values)

    # Commit the transaction and close the connection
    db.commit()
    db.close()


def handler(event=None, context=None):
    set_vessel_schedules()


if __name__ == "__main__":
    print(str(handler()))
