from selenium import webdriver
import time
import os
import math

link = "http://127.0.0.1:8000/about"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_id("city")
    input1.send_keys("Гродно")
    button = browser.find_element_by_name("send")
    button.click()
    time.sleep(5)
    button = browser.find_element_by_class_name("tyn")
    button.click()

finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла