import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver.navigate("file:///race_condition.html")
WebDriverWait(driver).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"
