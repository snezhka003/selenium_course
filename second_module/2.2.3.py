from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element(By.ID, "num1").text)
y = int(browser.find_element(By.ID, "num2").text)
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(x + y))

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(10)

browser.quit()
