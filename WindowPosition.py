import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https:/www.google.com")
# Access each dimension individually
    x = driver.get_window_position().get('x')
    y = driver.get_window_position().get('y')
    print(x)
    print(y)
# Or store the dimensions and query them later
#position = driver.get_window_position()
#x1 = position.get('x')
#y1 = position.get('y')
