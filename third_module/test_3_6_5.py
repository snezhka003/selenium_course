import pytest
from selenium.webdriver.common.by import By
import json
import time

@pytest.fixture(scope="session")
def load_account():
    # Открываем файл с конфигом в режиме чтения
    with open('account.json', 'r') as account_file:
        # С помощью библиотеки json читаем и возвращаем результат
        account = json.load(account_file)
        return account
    
class TestLogin:
    def test_authorization(self, browser, load_account):

        login = load_account['login_stepik']
        password = load_account['password_stepik']

        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        time.sleep(5)

        browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login").click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "img.navbar__profile-img")
        time.sleep(5)