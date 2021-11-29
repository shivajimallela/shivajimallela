from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.google.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

driver.quit()