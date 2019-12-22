from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math
import time


@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_parameterized_submission(browser, link):
    browser.get(link)

    time.sleep(3)

    answer = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea'))
    )
    answer.send_keys(str(math.log(int(time.time()))))

    submit_btn = browser.find_element_by_css_selector('.submit-submission')
    submit_btn.click()

    time.sleep(3)

    expected = 'Correct!'
    actual = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
    ).text

    assert expected == actual, f"expected '{expected}, but got '{actual}''"



