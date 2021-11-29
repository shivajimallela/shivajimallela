from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https:/www.google.com")
    driver.set_window_size(1024, 759)
