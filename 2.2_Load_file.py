from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')
browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_element = browser.find_element_by_css_selector('[name="firstname"]')
    first_element.send_keys("Вася")
    second_element = browser.find_element_by_css_selector('[name="lastname"]')
    second_element.send_keys("Пупович")
    third_element = browser.find_element_by_css_selector('[name="email"]')
    third_element.send_keys("Pupovicham@net.com")
    file = browser.find_element_by_css_selector('#file')
    file.send_keys(file_path)

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
