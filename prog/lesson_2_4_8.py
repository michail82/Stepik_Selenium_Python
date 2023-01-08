from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

browser.implicitly_wait(5)

browser.execute_script("window.scrollBy(0, 350);") # Скролим страницу вниз

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

try:
    WebDriverWait(browser, 12) .until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    button = browser.find_element(By.ID, "book")
    button.click()

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