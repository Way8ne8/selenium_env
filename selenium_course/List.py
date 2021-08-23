from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x, y):
    return str(x + y)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)

    z = calc(x, y)
    select = Select(browser.find_element_by_id('dropdown'))
    input1 = select.select_by_value(z)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()
    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()
