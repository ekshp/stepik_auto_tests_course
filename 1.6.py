from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
#     input4.send_keys("Russia")
#     input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
#     input5.send_keys("Russia")
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# import math
#
#
# def calc(z):
#     return str(math.log(abs(12*math.sin(int(z)))))
#
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/get_attribute.html')
# x_element = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
# x = x_element
# y = calc(x)
# browser.find_element(By.ID, 'answer').send_keys(y)
# browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
# browser.find_element(By.ID, "robotCheckbox").click()
# time.sleep(10)
# browser.quit()
url = 'https://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(url)

num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text
answer = int(num1) + int(num2)
print(answer)

browser.find_element(By.ID, 'dropdown').click()
Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(answer))
browser.find_element(By.ID, 'dropdown').click()
browser.find_element(By.CSS_SELECTOR, 'button').click()
time.sleep(5)