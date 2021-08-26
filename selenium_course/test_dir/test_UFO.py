import pytest
from selenium import webdriver
import time
import math

# @pytest.fixture(scope="function")
# def browser():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     browser = webdriver.Chrome(options=options)
#     browser.implicitly_wait(10)
#     yield browser
#
#     browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_ufo_search(browser, link):
    link1 = f"{link}"
    browser.get(link1)
    #time.sleep(5)
    area = browser.find_element_by_css_selector(".ember-text-area")
    answer = math.log(int(time.time()))
    area.send_keys(str(answer))
    #time.sleep(5)
    butt = browser.find_element_by_css_selector(".submit-submission")
    butt.click()
    result = browser.find_element_by_css_selector(".smart-hints__hint")
    assert result.text == "Correct!", "Ответ неправильный"

