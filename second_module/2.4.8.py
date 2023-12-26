# В этой задаче нужно написать программу, которая будет выполнять следующий сценарий:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # 3. Нажать на кнопку "Book"
    browser.find_element(By.ID, "book").click()
    # 4. Решить уже известную математическую задачу (используйте ранее написанный код)...
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    # ...и отправить решение
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(2)
    browser.quit()
