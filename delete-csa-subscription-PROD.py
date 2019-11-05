#
# Deletes the current subscriptions for a VM
#
# Author: Jason Crandall


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variables: Enter the password needed to login here
user = ""
password = ""
url = ""

browser = webdriver.Chrome()
actions = ActionChains(browser)

# Opens the Login page for the website
browser.get(url)

WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "icon-refresh")))
browser.find_element_by_name("action_login").click()

# Login to the CSA front end with the monitoring account
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
browser.find_element_by_name("username").send_keys(user)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_name("submit").click()

# Opens the all subscriptions button
WebDriverWait(browser, 45).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollbox"]/div/div/div/div[1]/mpp-section[1]/div/div/div/div/mpp-tile[1]/div/a/h6/strong')))
WebDriverWait(browser, 45).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="scrollbox"]/div/div/div/div[1]/mpp-section[1]/div/div/div/div/mpp-tile[1]/div/a/h6/strong'))).click()
WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.NAME, 'refresh')))

time.sleep(2)

# Loops until all of the subscriptions have been deleted
try:
    
    while ((bool(browser.find_element_by_name('subscriptions_list')))):

        try:
            if (bool(browser.find_element_by_name('action_cancel'))):
                while (bool(browser.find_element_by_name('action_cancel'))):
                    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, 'action_cancel'))).click()
                    time.sleep(2)
                    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.NAME, 'action_confirm_cancel')))
                    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, 'action_confirm_cancel'))).click()
                    time.sleep(2)
        except Exception:
            pass

        time.sleep(3)

        try:
            if (bool(browser.find_element_by_name('action_delete'))):
                while (bool(browser.find_element_by_name('action_delete'))):
                    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, 'action_delete'))).click()
                    time.sleep(2)
                    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.NAME, 'action_confirm_delete')))
                    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, 'action_confirm_delete'))).click()
                    time.sleep(2)
        except Exception:
            pass

        time.sleep(3)
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, 'refresh'))).click()
        time.sleep(1)

except Exception:
    time.sleep(2)
    browser.quit()

