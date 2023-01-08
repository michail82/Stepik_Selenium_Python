import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)
  
    button = browser.find_element (By.CSS_SELECTOR, "[type='submit']")
    button.click() 
   
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = calc(x_element.text)
   
    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)
    
    button = browser.find_element (By.XPATH, '//button[text()="Submit"]')
    button.click()
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()


