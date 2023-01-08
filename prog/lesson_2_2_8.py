import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html" 

print ("Start program *******************************************")

try:
    browser = webdriver.Chrome()
    browser.get(link)
  
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Имя')
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Фамилия')
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('111@www.ua')
  
  
    browser.execute_script("window.scrollBy(0, 350);") # Скролим страницу вниз
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    
    button = browser.find_element (By.XPATH, '//button[text()="Submit"]')
    button.click() 
   
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


print ('Программа завершина') 
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))