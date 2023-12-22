from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
browser.find_element(By.ID, "answer").send_keys(calc(x))
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
button.click()

time.sleep(10)

browser.quit()
