from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.google.com")

ele = driver.find_element(By.CSS_SELECTOR, 'body')

# Returns and base64 encoded string into image
ele.screenshot('./image.png')

driver.quit()
