from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver :
    driver.get("https://www.amazon.in/")
    cook = (driver.get_cookies())
    print(len(cook))
    print(cook)

cook = {'name':'kur','sch': 'sis','kei':'loc'}
#driver.add_cookie(cook)

# adding new cookies to broweser
cook = driver.get_cookies()
print(len(cook))
print(cook)
driver.quit()