from selenium import webdriver
from pages.login_page import LoginPage
import time

driver = webdriver.Firefox()

# --- Login ---
login_page = LoginPage(driver)
login_page.open()
login_page.login("standard_user", "secret_sauce")
login_page.verify_login()

time.sleep(2)
driver.quit()
print("✅ Test finished and browser closed.")