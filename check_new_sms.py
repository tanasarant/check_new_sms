import requests, json, time
from session_id import login_and_get_session
from router_info import ROUTER_URL, HEADERS

def check_new_sms(ROUTER_URL, COOKIES, HEADERS):
    try:
        resp = requests.get(ROUTER_URL, cookies=COOKIES, headers=HEADERS, timeout=5)
        data = resp.json()

        return data

    except Exception as e:
        print("Error:", e)
        return None

#### MAIN ####
    
session_id = login_and_get_session()
print(session_id)

# Cookies from your browser
COOKIES = {
    "clear_web_language": "0",
    "qSessId": session_id,
    "DWRLOGGEDID": session_id,
    "DWRLOGGEDUSER": "admin",
    "DWRLOGGEDTIMEOUT": "300",
    "clear_pageNum": "0",
    "clear_pageIndex": "1"
}

data = check_new_sms(ROUTER_URL, COOKIES, HEADERS)
print("data is: ", type(data))