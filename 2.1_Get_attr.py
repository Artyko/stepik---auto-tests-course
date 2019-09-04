from selenium import webdriver
import time
import math


def calc(variable):
    return str(math.log(abs(12*math.sin(int(variable)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector('#treasure').get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click()
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
