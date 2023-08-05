CORRECT_DATE_FORMAT = "%m/%d/%y"
PARSE_DATE_FORMAT_LBCT = '%m/%d/%Y %H:%M'
PARSE_DATE_FORMAT_PIERA = '%m/%d/%Y %H:%M'
PARSE_DATE_FORMAT_FENIX = '%b-%d-%y %H%M'
PARSE_DATE_FORMAT_PCT = '%m/%d/%Y %I:%M %p'
PARSE_DATE_FORMAT_ITS = '%m/%d/%Y %H:%M'
PARSE_DATE_FORMAT_YTI = '%m/%d/%Y'
PARSE_DATE_FORMAT_TRAPAC = 'm/%d/%Y %H:%M'
PARSE_DATE_FORMAT_TTI = '%m/%d/%Y %H:%M'


LBCT_URL = 'https://www.lbct.com/Operations/getVesselScheduleJson'
LBCT_COLUMN_VALUES = ['terminal', 'vessel', 'arrival', 'etd']
LBCT_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


PIERA_URL = 'https://piera.tideworks.com/fc-PA/home/default.do'
PIERA_COLUMN_VALUES = ['terminal', 'Vessel Name', 'ETA', 'ETD']
PIERA_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


PIERA_LOGIN_FIRST_URL = 'https://piera.tideworks.com/fc-PA/default.do'
PIERA_LOGIN_SECOND_URL = 'https://piera.tideworks.com/fc-PA/js/ajax.jsp'
PIERA_LOGIN_THIRD_URL = 'https://piera.tideworks.com/fc-PA/j_spring_security_check'


FENIX_URL = 'https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vS0DQlzD951t7yCembZjG2DyIGkKSSXbW_j29t9csc2oFcLMi-iuEg3tX3cZWIdHmGh0rO9meIp--az/pubhtml/sheet'
FENIX_COLUMN_VALUES = ['terminal', 'vessel', 'eta', 'etd']
FENIX_COLUMN_DF = ['vessel', 'Service', 'Line', 'Visit', 'eta', 'ATA', 'etd', 'ATD', 'Empty Pickup', 'Begin Receive', 'DryCutoff']


PCT_URL = 'https://pct.tideworks.com/fc-PCT/home/default.do'
PCT_COLUMN_VALUES = ['terminal', 'Vessel Name', 'ETA', 'ETD']
PCT_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


PCT_LOGIN_FIRST_URL = 'https://pct.tideworks.com/fc-PCT/home/default.do'
PCT_LOGIN_SECOND_URL = 'https://pct.tideworks.com/fc-PCT/j_spring_security_check'


ITS_URL = 'https://tms.itslb.com/tms2/Vessel/VesselSchedule'
ITS_COLUMN_VALUES = ['terminal', 'Vessel Name', 'Arrival', 'Departure']
ITS_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


ITS_LOGIN_FIRST_URL = 'https://tms.itslb.com/tms2/Account/Login'
ITS_LOGIN_SECOND_URL = 'https://tms.itslb.com/tms2/Account/Login'


ETS_URL = 'https://www.etslink.com/'
ETS_COLUMN_VALUES = ['terminal', 'Vessel', 'ETA', 'ETD']
ETS_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


APM_FIRST_URL = 'https://www.apmterminals.com/en/los-angeles/online-services/vessel-schedule'
APM_SECOND_URL = 'https://www.apmterminals.com/apm/api/vesselscheduletable/vesselscheduletableresults'
APM_COLUMN_VALUES = ['terminal', 'vessel', 'eta', 'etd']
APM_COLUMN_DF = ['vessel', 'eta', 'etd']


YTI_URL = 'https://docs.google.com/spreadsheets/d/1YH4AaMqtlAaJ_MV8DgagVuNVFuohG3R6hkmPmfGpgRc/pubhtml'
YTI_COLUMN_VALUES = ['Terminal', 'Vessel Name', 'ETA', 'ETD']
YTI_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


WBCT_URL = 'https://voyagertrack.portsamerica.com/logon'
WBCT_COLUMN_VALUES = ['terminal', 'Vessel', 'ETA', 'ERD']
WBCT_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


CAPTCHA_SOLVING_SERVICE_KEY = '05606d79082e77d9616a6a72e72edb33'
TRAPAC_CAPTCHA_SITE_KEY = '6LfCy7gUAAAAAHSPtJRrJIVQKeKQt_hrYbGSIpuF'
TRAPAC_CAPTCHA_URL = 'https://www.trapac.com/quick-check/'
TRAPAC_URL = 'https://www.trapac.com/wp-admin/admin-ajax.php'
TRAPAC_CULUMN_DF_RESPONSE = ["Service", "Vessel", "Code", "Voyage", "ETA", "ETD", "ODR First Receiving", "Local First Receiving", "Cut Off", "Extended Late Gate", "Remark", "Unnamed"]
TRAPAC_COLUMN_VALUES = ['Terminal', 'Vessel', 'ETA', 'ETD']
TRAPAC_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


TTI_FIRST_REQUEST = 'https://www.ttilgb.com/main/index.do'
TTI_SECOND_REQUEST = 'https://www.ttilgb.com/uiAgs02Action/searchVesselScheduleList.do?selSscoId=MSC,HDM,MAE&strtDt={today}&endDt={next_month}&acssHis=USLGB,0245APP,0346001,undefined'
TTI_COLUMN_VALUES = ['Terminal', 'vslNm', 'etaDt', 'etdDt']
TTI_COLUMN_DF = ['terminal', 'vessel', 'eta', 'etd']


VESSEL_MASTER_COLUMN_VALUES = ["terminal", "vessel", "eta", "etd"]
VESSEL_MASTER_COLUMN_DF = ["terminal", "vessel", "eta", "etd", "last_updated"]