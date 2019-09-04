from selenium import webdriver
import time


browser = webdriver.Chrome()
try:

    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector('input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла