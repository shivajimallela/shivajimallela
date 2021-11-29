import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https:/www.google.com")
    driver.set_window_position(265, 356)
    time.sleep(20)
    driver.minimize_window()
    time.sleep(10)
    driver.maximize_window()
    time.sleep(10)
    driver.fullscreen_window()
