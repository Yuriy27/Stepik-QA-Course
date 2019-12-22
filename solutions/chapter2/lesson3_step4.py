from selenium import webdriver
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    j = browser.find_element_by_tag_name("button")
    j.click()

    

    #time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)

    sb = browser.find_element_by_tag_name("button")
    sb.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
