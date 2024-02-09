from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os


def calc(y):
    return str(math.log(abs(12*math.sin(int(y)))))


url = 'http://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    # alert = browser.switch_to.alert
    # alert.accept()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(5)
