import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()