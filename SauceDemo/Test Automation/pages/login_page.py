from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Navigate to test website ---
    def open(self):
        self.driver.get("https://saucedemo.com/")

    # --- Perform login ---
    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # --- Wait for inventory page to confirm login success ---
    def verify_login(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_list")))
        print("✅ Login successful — Inventory page loaded.")
