from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Wait until inventory list is visible ---
    def verify_list(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_list")))

    # --- Sort selection ---
    def sort_option(self, option_value):
        dropdown = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product_sort_container")))
        dropdown.click()
        dropdown.find_element(By.CSS_SELECTOR, f"option[value='{option_value}']").click()

    # --- Return list of products by name ---
    def get_products_names(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR,".inventory_item_name")
        product_names = []
        for el in product_elements:
            product_names.append(el.text)
        return product_names

    # --- Return list of prices ---
    def get_prices(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR,".inventory_item_price")
        product_prices = []
        for el in price_elements:
            price_text = el.text.replace("$", "")
            price = float(price_text)
            product_prices.append(price)
        return product_prices

    # --- Verify sort elements ---
    def verify_order(self, sort_type, elements):

        sort_labels = {
            "az": "Name (A to Z)",
            "za": "Name (Z to A)",
            "lohi": "Price (Low to High)",
            "hilo": "Price (High to Low)"
        }

        label = sort_labels.get(sort_type, sort_type)

        # --- verify Low to High and High to Low ---
        if sort_type in ["lohi", "hilo"]:
            if sort_type == "lohi":
                expected = sorted(elements)
            else:
                expected = sorted(elements, reverse=True)

        # --- verify A to Z and Z to A ---
        elif sort_type in ["az", "za"]:
            if sort_type == "az":
                expected = sorted(elements)
            else:
                expected = sorted(elements, reverse=True)

        # --- verify invalid input in test ---
        else:
            raise ValueError(f"❌ Unsupported sort_type: {label}")

        is_sorted = elements == expected

        # --- return bool statement to assert ---
        if is_sorted:
            print(f"✅ Elements correctly sorted for type: {label}")
        else:
            print(f"❌ Elements NOT sorted correctly for type: {label}")
        return is_sorted



