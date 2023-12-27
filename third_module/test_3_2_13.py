import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestsRegistration(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        print('setup executed')

    def tearDown(self):
        self.browser.quit()
        print('teardown executed')
        
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        self.browser.find_element(By.CLASS_NAME, "first:required").send_keys("Text")
        self.browser.find_element(By.CLASS_NAME, "second:required").send_keys("Text")
        self.browser.find_element(By.CLASS_NAME, "third:required").send_keys("Text")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Values should be equal")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        self.browser.find_element(By.CLASS_NAME, "first:required").send_keys("Text")
        self.browser.find_element(By.CLASS_NAME, "second:required").send_keys("Text")
        self.browser.find_element(By.CLASS_NAME, "third:required").send_keys("Text")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Values should be equal")
        
if __name__ == "__main__":
    unittest.main()