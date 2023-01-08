import math
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html" 
print ("Start program *******************************************")
try:
  browser = webdriver.Chrome()
  browser.get(link)
  
  x_element = browser.find_element(By.ID, "input_value")
  y = calc(x_element.text)

  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)
  
  
  browser.execute_script("window.scrollBy(0, 300);") # Скролим страницу вниз
  
  option1 = browser.find_element(By.ID, "robotCheckbox")
  option1.click()
  option2 = browser.find_element(By.ID, "robotsRule")
  option2.click()
   
  button = browser.find_element (By.XPATH, '//button[text()="Submit"]')
  button.click() 
   
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


print ('Программа завершина') 
