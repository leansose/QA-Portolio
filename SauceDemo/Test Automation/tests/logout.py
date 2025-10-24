from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# --- Login ---
login_page = LoginPage(driver)
login_page.open()
login_page.login("standard_user", "secret_sauce")
login_page.verify_login()

# --- Logout ---
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-burger-menu-btn"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logout_sidebar_link"))).click()

# --- Verify logout success ---
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root")))
print("✅  Back to Login page")

time.sleep(2)
driver.quit()
print("✅  Test finished with success Logout.")