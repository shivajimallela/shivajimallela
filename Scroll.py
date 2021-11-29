import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

#driver.execute_script("window.scrollBy(0,1000)","")

pic = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/div[14]/div/div/div[2]/div/ul/li[3]/span/a/img')

driver.execute_script("arguments[0].scrollIntoView();",pic)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)

driver.quit()