from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(variable):
    return str(math.log(abs(12*math.sin(int(variable)))))


browser = webdriver.Chrome()
browser.implicitly_wait(5)
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("#book")
    button.click()

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
