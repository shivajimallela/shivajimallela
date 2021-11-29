from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https:/www.google.com")
    #    size = driver.get_window_size()
    width = driver.get_window_size().get('width')  # or we can write; width = size.get("width")
    height = driver.get_window_size().get('height') # or we an write; height = size.get("height")


    print(width)
    print(height)

