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

# --- Add product ---
product_selector = "#add-to-cart-sauce-labs-backpack"
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, product_selector))).click()

# --- Verify product added ---
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#remove-sauce-labs-backpack")))
print("✅ Product added successfully.")

# --- Open cart and verify products on cart ---
driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
wait.until(EC.url_contains("cart"))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_item")))
print("🛒 Cart page loaded with item(s).")

# --- Checkout flow ---
driver.find_element(By.CSS_SELECTOR,"#checkout").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name"))).send_keys("Leandro")
driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Sousa")
driver.find_element(By.CSS_SELECTOR,"#postal-code").send_keys("4425-057")
driver.find_element(By.CSS_SELECTOR,"#continue").click()

# --- Finish order and back to products ---
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#finish"))).click()
print("✅ Checkout completed successfully.")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#back-to-products"))).click()

time.sleep(2)
driver.quit()
print("✅ Test finished with success Logout.")



