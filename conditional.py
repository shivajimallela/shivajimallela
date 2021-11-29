from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://accounts.lambdatest.com/login')

id = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[1]/input")
#pas = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/div[2]/div/input")

id.send_keys('mallela.praveen0@gmail.com')
#pas.send_keys('Shivaji@903058')"/html/body/div[1]/div/div/div/div/form/div[1]/input"

print(id.is_enabled())
print(id.is_displayed())
#print(pas.is_displayed())
#print(pas.is_enabled())
driver.close()