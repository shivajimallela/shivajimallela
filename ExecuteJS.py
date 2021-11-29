from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https:/www.google.com")
# Stores the header element
header = driver.find_element(By.CSS_SELECTOR, "body")

# Executing JavaScript to capture innerText of header element
driver.execute_script('return arguments[0].innerText', header)
