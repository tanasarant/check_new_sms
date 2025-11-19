from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from router_credential import ROUTER_USERNAME, ROUTER_PASSWORD

ROUTER_URL = "http://192.168.100.1/"
# USERNAME = "admin"
# PASSWORD = "normal_human_passwd"   # the normal human password

def login_and_get_session():
    service = Service("/usr/local/bin/geckodriver")  # adjust if needed
    driver = webdriver.Firefox(service=service)

    driver.get(ROUTER_URL)
    time.sleep(1)

    # Fill username
    driver.find_element(By.ID, "username").send_keys(ROUTER_USERNAME)

    # Fill password
    driver.find_element(By.ID, "password").send_keys(ROUTER_PASSWORD)

    # Click Login
    driver.find_element(By.ID, "BTN_Login").click()
    time.sleep(2)

    # Extract session cookie (qSessId)
    cookies = driver.get_cookies()
    driver.quit()
    for c in cookies:
        if c["name"] == "qSessId": return c["value"]
        else: return None