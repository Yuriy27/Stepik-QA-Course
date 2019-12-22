from selenium import webdriver
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_css_selector("[name='firstname']")
    a.send_keys('rr')

    b = browser.find_element_by_css_selector("[name='lastname']")
    b.send_keys('rr')

    c = browser.find_element_by_css_selector("[name='email']")
    c.send_keys('rr')

    f = browser.find_element_by_css_selector("[name='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')

    f.send_keys(file_path)

    sbmt = browser.find_element_by_tag_name("button")

    sbmt.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
