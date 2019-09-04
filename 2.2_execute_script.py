from selenium import webdriver
import time
import math


def calc(variable):
    return str(math.log(abs(12*math.sin(int(variable)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')

    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    answer.send_keys(y)
    check = browser.find_element_by_css_selector("[for='robotCheckbox']")
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
