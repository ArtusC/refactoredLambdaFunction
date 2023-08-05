PIERA_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'BNI_JSESSIONID=000000000000000000000000fafd14ac0000921f; JSESSIONID=0C473AD24444033D1FA693F2BE951F14; BNI_JSESSIONID=000000000000000000000000fafd14ac0000921f; __utmc=218720536; __utmz=218720536.1678376150.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=218720536.124420360.1676523294.1678376150.1678383134.5; __utmt=1; __utmt_b=1; __utmb=218720536.4.10.1678383134',
    'Referer': 'https://piera.tideworks.com/fc-PA/home/default.do?method=scheduleSubmit',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


PIERA_PARAMS = {
    'method': 'scheduleAsList',
    'line': '',
    'vesselVoyage': '',
    'eta': '',
    'etd': '',
}


PIERA_LOGIN_FIRST_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


PIERA_LOGIN_SECOND_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'BNI_JSESSIONID=000000000000000000000000fafd14ac0000921f',
    'Referer': 'https://piera.tideworks.com/fc-PA/default.do',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

PIERA_LOGIN_SECOND_REQUEST_PARAM = {
    'version': '95014203010320232238',
}


PIERA_LOGIN_THIRD_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=D002DB595BE15890D7E5A15BF7D561A4; BNI_JSESSIONID=000000000000000000000000fafd14ac0000921f; __utma=218720536.698675289.1676172707.1676172707.1676172707.1; __utmc=218720536; __utmz=218720536.1676172707.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=218720536.1.10.1676172707',
    'Origin': 'https://piera.tideworks.com',
    'Referer': 'https://piera.tideworks.com/fc-PA/default.do',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


PIERA_LOGIN_THIRD_REQUEST_PARAM = {
    'j_username': 'username',
    'j_password': 'username',
}


FENIX_COOKIES = {
    '__Secure-3PSID': 'Twii0ARUgThpeaW-SI-j-vobmkM8QJ5oFs1vLvbtioF07UUx5K2lwvnl_i_QiT3WAwsNQw.',
    '__Secure-3PAPISID': '_YUfRXl3BPDacSRs/AUfL3royrEjbUJkKz',
    'NID': '511=awyXikrdc1qSlhS7oRl4BH0AjVXyMxKBGdSIQDmwIP8HxIV_X1x44zKuJRLQ3295EGJ1_gQb6oAPP5h1P0mmPdSKvB8Kb2X-Ae7ftL2TNwLVhH5cahk1D1jSrY8A4YewkBoSl75Lzh56cYYa4n-K8AUV57leE7gktRNnH136MKLeVdnLeUcTZ0bVqTnEED3I6O8hfArozd8h1ewBvkC-MvzUWXXKQhCZkHzicu5FgmytttIIOQ1KwP6m2W5fnxGAmSp95A1NtFCWzcpWnqE5gz9swggm4h0FEe-wPJFGSKzdzpXqsqcYaq0',
    '1P_JAR': '2023-02-17-17',
    '__Secure-3PSIDCC': 'AFvIBn_S6sYqHpos1jg30OX6pnXSpEfHSU3pdVjPkzMm8vW8QnY7w_dzQBl17hJhcAz5RmBFkA7g',
}


FENIX_HEADERS = {
    'authority': 'docs.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__Secure-3PSID=Twii0ARUgThpeaW-SI-j-vobmkM8QJ5oFs1vLvbtioF07UUx5K2lwvnl_i_QiT3WAwsNQw.; __Secure-3PAPISID=_YUfRXl3BPDacSRs/AUfL3royrEjbUJkKz; NID=511=awyXikrdc1qSlhS7oRl4BH0AjVXyMxKBGdSIQDmwIP8HxIV_X1x44zKuJRLQ3295EGJ1_gQb6oAPP5h1P0mmPdSKvB8Kb2X-Ae7ftL2TNwLVhH5cahk1D1jSrY8A4YewkBoSl75Lzh56cYYa4n-K8AUV57leE7gktRNnH136MKLeVdnLeUcTZ0bVqTnEED3I6O8hfArozd8h1ewBvkC-MvzUWXXKQhCZkHzicu5FgmytttIIOQ1KwP6m2W5fnxGAmSp95A1NtFCWzcpWnqE5gz9swggm4h0FEe-wPJFGSKzdzpXqsqcYaq0; 1P_JAR=2023-02-17-17; __Secure-3PSIDCC=AFvIBn_S6sYqHpos1jg30OX6pnXSpEfHSU3pdVjPkzMm8vW8QnY7w_dzQBl17hJhcAz5RmBFkA7g',
    'referer': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0DQlzD951t7yCembZjG2DyIGkKSSXbW_j29t9csc2oFcLMi-iuEg3tX3cZWIdHmGh0rO9meIp--az/pubhtml?gid=0&single=true&widget=true&headers=false',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-chrome-connected': 'source=Chrome,id=112371467252451733950,mode=0,enable_account_consistency=false,consistency_enabled_by_default=false',
    'x-client-data': 'CIe2yQEIpLbJAQjBtskBCKmdygEIkY3LAQiVocsBCPGAzQE=',
}


FENIX_PARAMS = {
    'headers': 'false',
    'gid': '0',
}


PCT_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=CB8A9997C8FB59C379E51D5BEE4E6E5E; BNI_JSESSIONID=aJhuFD39VaPmhsRcyl1o1s0yU1It5TvfQXk3-K9P2THD-p7NJx-X5UhRfF6lYrJk1n8oh0NNDeOlnOayKzwwdg==; __utmc=152605880; __utmz=152605880.1678316916.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=152605880.2068071920.1678316916.1678376376.1678401025.4; __utmt=1; __utmt_b=1; __utmb=152605880.9.10.1678401025',
    'Referer': 'https://pct.tideworks.com/fc-PCT/home/default.do?method=scheduleSubmit',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


PCT_PARAMS = {
    'method': 'scheduleAsList',
    'line': '',
    'vesselVoyage': '',
    'eta': '',
    'etd': '',
}


PCT_LOGIN_FIRST_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


PCT_LOGIN_SECOND_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=3BE31C60137364F2D206B7FC2E35AD18; BNI_JSESSIONID=aJhuFD39VaPmhsRcyl1o1s0yU1It5TvfQXk3-K9P2THD-p7NJx-X5UhRfF6lYrJk1n8oh0NNDeOlnOayKzwwdg==; __utma=152605880.15437413.1676178744.1676178744.1676178744.1; __utmc=152605880; __utmz=152605880.1676178744.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=152605880.1.10.1676178744',
    'Origin': 'https://pct.tideworks.com',
    'Referer': 'https://pct.tideworks.com/fc-PCT/default.do',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


PCT_LOGIN_SECOND_REQUEST_PARAM = {
    'j_username': 'username',
    'j_password': 'password',
}


ITS_HEADERS = {
    'authority': 'tms.itslb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__RequestVerificationToken_L3RtczI1=YXBtulFKyfcmEjQEy1nbhJxlxpc2HyiPeyPIipIlNLODm-z7Z_MtEyTiFyZJGXiyT-adpRQGBn0FCjs3whd6ADrwdSCkZMHmru5sAfekkPk1; .AspNet.ApplicationCookie=L5l92iIc6zH1SlceDTWlmavAU3C0h5_p8uizbuizfWvzOj204Gl0ltSPudI6lj7E6dyPeiCc_6w9PKza_cPEYv2XpgG8eyL_BIKzh9Eoxl6v3GxK4gwB_PSn-cEiEo7xkcMU5P0IPGQ5z2KjJ5-nm2b7nnAgV9SARO_SamsdHKXvpWOox4CmJBS-qQU3W-eeDHuKluXd9jKMxDHnG8BILRUczULsC-kwFqmbkKuSGlrmLXreap4FJT-DeNuxwmne506CfB9Dh6pE1WCKLqTT23cuJKwvA0WBnrScGmqxc6s_BYCtlWpHV5v1athzLH8ohrvyGbM5aN3K9ZXIQLRylPJUKQFYCbLlzr2cn4MIodClEeBJpAnVDzNDzC7CeD-bc9xHpdrK3rkaxFlGhnXlbkIGWGcoCkoWz8vv2YDIR9py-hFRzzNArJ4BuYqt7Rkq8u9z7auesYLQQcpOEXQSv4Bsy0LGA8gdXUN7vNCAVL4FO3GRTPm4IdaJtmkXjQTw_N0CXkc_rl8fvhnqjAb_snFxaKix0J_g7bcjQqPjOlpfHb3Uo0vV7iwWBCcgUC_cIi_DI7hasnmulwcEPuru4T8ecPfw9EURDKXMX0LHnogHTxHyOdw4HFYmMRnWAHYkaZRMrXk8PincTYNGtvOifHfU06QfhdSWMfPzW-qvj6LbLutDJVIbnjFW0aeAUtf5Po3zZ1Vsya2akWs5oqSdcSaRZboIURlUHizWXG6aSsScFbJLmyA0oSNyNEs-I2QIF8mQqPOpzHv2pD83DeaHyulbhWB1CW6d7hIGKUBax0pvzkMF93Wifsh13A2yAjjilEMqsJ2aY0lN-QhGIMV0H_YAXw5eJh4xmcQ0cIqyQC2w1T8msQrT00ayXfmt0aDKkvAVF0ecKe3Gko3dta1tENHmtUIniI0nqCrYcyHGRdytPeIR9x2yDl5feR9PJbfJO-2SJAONgm2SiXuBWIxj35FwSzE5AcqyCpoW60Ktw85pnbMpvFUH16Z8zKjFXCqob1oEDBap4VdnpAYISUP7thL9eLJxxNVNNrJU2it5h8kZ686zEYlxhMbvvkm1E0IVOMUC2ygNqa6Ut-OBITNSAuqJS1dzkCz9ihmcE_dUnQBs-6WtN--aBHPTprsO_Nr8R4MJoE4UR15Ul4543R13hN5AXyd00gOBhAj8jbWN4TtIbFU14Tb5FaDE6o53LSn-IySAkoO7sRBJWKvYp07thos3kYm2wQ8L2kKqOHOo56E-Mawb4vAuPbOp_odM72Y3K6U437VMfsLGw4gSmVpTv4TW8uyE1ttjiDhxVBqPUMDMQ89ZIZHaz4BUbw4kRtiZz7RZPPMfSnX0EGdVX8N-t5q_sQuHIaFA--M7IAtQUpbtJkMX8eca6f3zw3eEQrvV',
    'referer': 'https://tms.itslb.com/tms2/Account/Login?ReturnUrl=%2Ftms2%2FVessel%2FVesselSchedule',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


ITS_LOGIN_FIRST_HEADERS = {
    'authority': 'tms.itslb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://tms.itslb.com/tms2/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


ITS_LOGIN_SECOND_HEADERS = {
    'authority': 'tms.itslb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__RequestVerificationToken_L3RtczI1=RDtFG4niX16VNO4gbYal0byCBuGLkPDt0-FabXPGdKTbfpDDLsRobnavu3Pfkz4dj0i9T5WT5GAMmfGYdw7fAOpZag0suHHV6A-8cmUeFrM1',
    'origin': 'https://tms.itslb.com',
    'referer': 'https://tms.itslb.com/tms2/Account/Login',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


ITS_LOGIN_PARAMS = {
    '__RequestVerificationToken': 'TOKEN_HERE',
    'UserName': 'username',
    'Password': 'password',
}


ETS_COOKIES = {
    'JSESSIONID': 'D0E0FBEC746DFB08F0357508ABA72E5B',
}


ETS_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=D0E0FBEC746DFB08F0357508ABA72E5B',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


APM_FIRST_HEADERS = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


APM_SECOND_HEADERS = {
    'authority': 'www.apmterminals.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.apmterminals.com/en/los-angeles/online-services/vessel-schedule',
    'cookies': 'COOKIES_HERE',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'site-id': 'c56ab48b-586f-4fd2-9a1f-06721c94f3bb',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


APM_PARAMS = {
    'TerminalId': 'c56ab48b-586f-4fd2-9a1f-06721c94f3bb',
}


YTI_HEADERS = {
    'authority': 'docs.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://yti.com/services/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


YTI_PARAMS = {
    'gid': '1244946891',
    'single': 'true',
    'widget': 'false',
    'headers': 'false',
}


WBCT_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


WBCT_PARAMS = {
    'siteId': 'WBCT_LA',
}


TRAPAC_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


TRAPAC_PAYLOADS = {
    'action': 'trapac_transaction',
    'recaptcha-token': 'TOKEN_SOLUTION_HERE',
    'terminal': 'LAX',
    'transaction': 'vessel_schedules',
    'containers': "",
    'container': '',
    'booking': '',
    'email': '',
    'equipment_type': 'CT',
    'history_type': 'N',
    'services': '',
}


TTI_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# ---------------------------- #
PROXY_CONNECTIONS = {
    "http": "http://username.smartproxy.com:7000",
    "https": "http://password.smartproxy.com:7000"
}
# ---------------------------- #
