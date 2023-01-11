import time

import timer as timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expected_list=['Cucumber - 1 Kg','Rasberry -1/4 Kg','Strawberry - 1/4 Kg']
product_list=[]
serviceObject = Service("C:\Driver\chromedriver108.exe")

driver = webdriver.Chrome(service=serviceObject)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
time.sleep(5)
products=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for item in products:
    product_list.append(item.find_element(By.XPATH, "//h4[@class='product-name']").text)
print(product_list)
