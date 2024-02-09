from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os


def calc(y):
    return str(math.log(abs(12*math.sin(int(y)))))


url = 'https://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(url)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'new.txt')
browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Name')
browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Lastname')
browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Name@lastname.com')
browser.find_element(By.ID, 'file').send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, 'button').click()
time.sleep(5)
