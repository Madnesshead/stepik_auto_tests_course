from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element_by_id('book')
    button.click()
    x_element = browser.find_element_by_id('input_value').text
    result = calc(x_element)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(result)
    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()