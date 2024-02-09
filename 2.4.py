from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import math
import os


def calc(y):
    return str(math.log(abs(12*math.sin(int(y)))))


url = "http://suninjuly.github.io/explicit_wait2.html"

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get(url)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'solve').click()
    time.sleep(5)

