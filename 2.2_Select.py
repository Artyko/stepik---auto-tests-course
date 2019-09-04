from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def calc(variable_1, variable_2):
    return str(int(variable_1) + int(variable_2))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_1 = browser.find_element_by_css_selector('#num1').text
    x_2 = browser.find_element_by_css_selector('#num2').text
    y = calc(x_1, x_2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)
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