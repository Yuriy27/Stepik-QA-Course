from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)
    time.sleep(1)

    sbmt = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", sbmt)


    r_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    r_checkbox.click()

    r_rule_radio = browser.find_element_by_css_selector("#robotsRule")
    r_rule_radio.click()

    

    sbmt.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
