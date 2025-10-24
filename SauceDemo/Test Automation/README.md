# 🧪 SauceDemo Test Automation (Python + Selenium)

This project contains automated UI tests for the [Sauce Demo](https://www.saucedemo.com/) e-commerce website, developed in **Python** using **Selenium WebDriver** and following the **Page Object Model (POM)** design pattern.

---

## 🎯 Current Test Coverage

The project currently automates the main user flows:

- 🔐 **Login** – Validates successful login for standard users
- 🛒 **Sorting Products** – Verifies sorting by name and price (A–Z, Z–A, Low–High, High–Low)  
- ✅ **Checkout** – Adds products to cart and completes the checkout process  

Additional tests will be added soon to expand coverage.

---

## ⚙️ Test Environment

- **Language:** Python 3.13  
- **Framework:** Selenium WebDriver  
- **Browser:** Mozilla Firefox (chosen due to Chrome security pop-up issues)  
- **OS Compatibility:** Windows

---

## 🧩 Design Notes

- Implements POM (Page Object Model) for cleaner structure and easier maintenance 
- Modular approach: login, sorting, and checkout are separated for clarity
- Explicit waits and sleeps ensure element visibility for demo reliability
- Future refactors will improve reporting, data management, and cross-browser supports

---

## 💡 Future Improvements

- Add conftest.py with browser fixtures for Pytest
- Parameterize credentials and test data
- Add negative test scenarios (invalid login, empty checkout, etc.)
