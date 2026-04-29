from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://web-scraping.dev/products")

time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, "product")

for product in products:
    name = product.find_element(By.TAG_NAME, "h3").text
    price = product.find_element(By.CLASS_NAME, "price").text
    print(name, price)

driver.quit()