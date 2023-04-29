#!/usr/bin/python3

import time, sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages/')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Enter auth info
USERNAME = "admin"
PASSWORD = "admin"

# Enter login url
LOGIN_URL = "http://192.168.1.1/cgi-bin/login_advance.cgi"

# Enter reboot url
REBOOT_URL = "http://192.168.1.1/cgi-bin/indexmain.cgi"

# Enter driver path (chromium)
DRIVER_PATH = "/Users/strife/chromedriver_mac_arm64/chromedriver"

########################################## Script ##########################################

print("Attempting Login")
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(LOGIN_URL)
driver.find_element(By.ID, "Loginuser").send_keys(USERNAME)
driver.find_element(By.ID, "LoginPassword").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()

# Verify login
try:
    check_login = driver.find_element(By.ID, "logoutBtn_icon")
    if check_login.is_displayed():
        print("Login Successful")
except NoSuchElementException as e:
    print("Login Failed")

driver.get(REBOOT_URL)
main = driver.find_element(By.ID, "maintenance")
a = ActionChains(driver)
a.move_to_element(main).perform()
reb = driver.find_element(By.ID, "maintenance-reboot")
a.move_to_element(reb).click().perform()
driver.switch_to.frame("mainFrame")
driver.find_element(By.ID, "Reboot").click()

time.sleep(4)