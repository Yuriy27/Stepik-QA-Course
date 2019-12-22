from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
    x = x_element
    y = calc(x)

    r_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    r_checkbox.click()

    r_rule_radio = browser.find_element_by_css_selector("#robotsRule")
    r_rule_radio.click()

    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)

    sbmt = browser.find_element_by_css_selector("button[type='submit']")
    sbmt.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
