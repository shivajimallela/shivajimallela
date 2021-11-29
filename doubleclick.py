from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("http://demo.guru99.com/test/simple_context_menu.html")

act = ActionChains(driver)

fele = driver.find_element(By.XPATH,'//*[@id="authentication"]/span')
ele = driver.find_element(By.XPATH,'//*[@id="authentication"]/button')

#act.move_to_element(ele).click().perform() #  click  operation by mouse

act.context_click(fele).perform() # to perform Right click mouse operation

act.double_click(ele).perform() # to perform double lick operation

#act.drag_and_drop("1st ele, 2nd ele")# drag and drop method

