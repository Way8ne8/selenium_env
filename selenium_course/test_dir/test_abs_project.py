import unittest

from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Smolensk@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_abs2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Smolensk@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()