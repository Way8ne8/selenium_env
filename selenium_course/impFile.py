import os
from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Smolensk@gmail.com")
    current_dir = os.path.dirname(__file__)
    impFile = os.path.join(current_dir, "1.txt")
    f = browser.find_element_by_id("file")
    f.send_keys(impFile)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()