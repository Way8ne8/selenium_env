from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()
    time.sleep(2)
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    z = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(z)
    browser.find_element_by_css_selector('button[type="submit"]').click()

    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()