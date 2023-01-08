import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

print ('@@@@@@@@@@@@@@@@@@@@@@@Stat program')

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)
  
    button = browser.find_element (By.CSS_SELECTOR, "[type='submit']")
    button.click() 
    
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
   
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
    
print ('#######################')
print (x)
