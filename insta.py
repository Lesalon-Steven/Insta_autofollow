from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException

import time

ACCOUNT_USERNAME = "the_nomad_traveller__"
ACCOUNT_PASSWORD = "Travel123!"
TARGET_ACCOUNT = "https://www.instagram.com/tembeakenyasafaris254/"
# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")

# time.sleep(500)
time.sleep(2)
accept_cookies = driver.find_element(By.XPATH,
                                     "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
accept_cookies.click()

time.sleep(4)
username_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username_field.send_keys(ACCOUNT_USERNAME)

password_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

full_path = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button'
save_info = driver.find_element(By.XPATH, full_path)
save_info.click()

time.sleep(5)
notif_button = driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
notif_button.click()

time.sleep(5)
driver.get(TARGET_ACCOUNT)

time.sleep(5)
followers = driver.find_element(By.XPATH,
                                '//a[@href="/tembeakenyasafaris254/followers/" and contains(text(), "followers")]')
followers.click()

# Scrolling the popup div that contains followers
time.sleep(5)

pop_up_div = driver.find_element(By.XPATH, '//div[@class="_aano"]')

for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", pop_up_div)
    time.sleep(2)

all_buttons = driver.find_elements(By.CSS_SELECTOR, value='._aano button')

# for button in all_buttons:
#     try:
#         button.click()
#         time.sleep(1.1)
#     # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
#     except ElementClickInterceptedException:
#         cancel_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
#         cancel_button.click()
