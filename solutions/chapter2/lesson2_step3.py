from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1").text
    num2 = browser.find_element_by_css_selector("#num2").text
    red = int(num1) + int(num2)

    ans = Select(browser.find_element_by_css_selector("#dropdown"))
    ans.select_by_value(str(red))
    
    sbmt = browser.find_element_by_css_selector("button[type='submit']")
    sbmt.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
