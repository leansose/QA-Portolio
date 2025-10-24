from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# --- Login ---
login_page = LoginPage(driver)
login_page.open()
login_page.login("standard_user", "secret_sauce")
login_page.verify_login()

# --- Sort Products ---

inventory_page = InventoryPage(driver)
inventory_page.verify_list()

# --- Sort by High to Low ---
inventory_page.sort_option("hilo")
time.sleep(1)
prices = inventory_page.get_prices()
inventory_page.verify_order("hilo", prices)

# --- Sort by Low to High ---
inventory_page.sort_option("lohi")
time.sleep(1)
prices = inventory_page.get_prices()
inventory_page.verify_order("lohi", prices)

# --- Sort by A to Z ---
inventory_page.sort_option("az")
time.sleep(1)
product_names = inventory_page.get_products_names()
inventory_page.verify_order("az", product_names)

# --- Sort by Z to A ---
inventory_page.sort_option("za")
time.sleep(1)
product_names = inventory_page.get_products_names()
inventory_page.verify_order("za", product_names)

time.sleep(2)
driver.quit()
print("✅ Test finished and browser closed.")

