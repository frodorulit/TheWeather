from selenium import webdriver
import time
import os
import math

link = "http://127.0.0.1:8000/contacts"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("tg")
    button.click()

finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл