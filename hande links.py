import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.get("https://www.selenium.dev/")

    links = driver.find_elements(By.TAG_NAME,'a')

    print(len(links))
    for link in links:
       print(link.text)

    driver.find_element(By.LINK_TEXT,"Documentation").click()
    driver.close()



