from datetime import datetime, timedelta, date
import time
from dateutil.relativedelta import relativedelta

import static

def parse_date_to_month_day_year(date, date_format):
    return datetime.strptime(date, date_format).strftime(static.CORRECT_DATE_FORMAT)


def save_response(file_name, response):
    with open(file_name, "w") as f:
        f.write(response.text)


def current_year():
    return datetime.now().year


def format_date_fenix(date_str):
    month_day = date_str[3:9]
    year = date_str[:2]
    time_str = date_str[-4:]
    
    formatted_date = f"{month_day}-{year} {time_str}"
    parsed_date = time.strptime(formatted_date, static.PARSE_DATE_FORMAT_FENIX)
    return time.strftime(static.CORRECT_DATE_FORMAT, parsed_date)


def format_date_trapac():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=1)
    next_month = next_day + relativedelta(months=1)

    return {
        'from_date': current_date.strftime("%Y-%m-%d"),
        'to_date': next_month.strftime("%Y-%m-%d")
    }


def format_date_tti():
    today = date.today()
    next_month = today.replace(month=today.month + 1)
    formatted_next_month = next_month.strftime('%m-%d-%Y')
    formatted_today = today.strftime('%m-%d-%Y')

    return formatted_today, formatted_next_month