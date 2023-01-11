import time

import timer as timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObject = Service("C:\Driver\chromedriver108.exe")

driver = webdriver.Chrome(service=serviceObject)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
time.sleep(5)
products=driver.find_elements(By.XPATH,"//div[@class='products']/div") #implict wait does not work in find elements
for product in products:
    product.find_element(By.XPATH,"div/button").click()
time.sleep(5)
#driver.find_element(By.XPATH,"//div/a[@class='cart-icon']").click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
#driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
#driver.find_element(By.XPATH,"//div[@class='cart-preview active']/div/button").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoInfo")))
response=driver.find_element(By.CLASS_NAME,"promoInfo").text
print(response)
assert response == "Code applied ..!"

prices=driver.find_elements(By.XPATH,"//tbody/tr/td[5]/p")
sum=0
for price in prices:
    sum+=int(price.text)
print(sum)

amount=driver.find_element(By.CSS_SELECTOR,".totAmt").text
print(amount)
assert sum == int(amount)

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
driver.find_element(By.XPATH,"//select/option[@value='Bangladesh']").click()
driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
time.sleep(5)

