from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://demo.guru99.com/test/radio.html")


status = driver.find_element(By.ID,'vfb-7-1').is_selected()
print(status)

status = driver.find_element(By.ID,'vfb-7-2').is_selected()
print(status)

status = driver.find_element(By.ID,'vfb-7-1').click()

status = driver.find_element(By.ID,'vfb-7-1').is_selected()
print(status)

status = driver.find_element(By.ID,'vfb-7-2').click()

status = driver.find_element(By.ID,'vfb-7-2').is_selected()
print(status)

driver.close()