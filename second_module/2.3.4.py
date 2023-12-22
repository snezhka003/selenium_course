from selenium import webdriver
from selenium.webdriver.common.by import By
""" import time """
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()
browser.switch_to.alert.accept()
x = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
print(browser.switch_to.alert.text) # выведет в консоль текст из "победного" алерта

""" time.sleep(10) """

browser.quit()
