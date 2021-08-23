from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    z = calc(x)

    input1 = browser.find_element_by_id('answer')
    _ = input1.location_once_scrolled_into_view
    input1.send_keys(z)
    option1 = browser.find_element_by_id("robotCheckbox")
    _ = option1.location_once_scrolled_into_view
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    _ = option2.location_once_scrolled_into_view
    option2.click()
    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()