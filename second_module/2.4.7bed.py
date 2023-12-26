# ожидаем, что тест упал на поиске элемента "verify_message" с итоговым сообщением: no such element: Unable to locate element: {"method":"id","selector":"verify_message"}

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()