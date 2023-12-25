from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Snezhanna")
browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Prasolova")
browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@test.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser.find_element(By.ID, "file").send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

time.sleep(10)

browser.quit()
