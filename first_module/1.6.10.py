""" дана страница с формой регистрации. Проверьте, что можно зарегистрироваться на сайте, 
заполнив только обязательные поля, отмеченные символом *: First name, last name, email. 
Текст для полей может быть любым. 
Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!" 
с текстом на странице, которая открывается после регистрации. 
Для сравнения воспользуемся стандартной конструкцией assert из языка Python. """
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CLASS_NAME, "first:required").send_keys("Text")
    browser.find_element(By.CLASS_NAME, "second:required").send_keys("Text")
    browser.find_element(By.CLASS_NAME, "third:required").send_keys("Text")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

""" Углубимся немного в использовании конструкции assert из данного примера. 
Если результат проверки "Поздравляем! Вы успешно зарегистрировались!" == welcome_text вернет значение False, 
то далее выполнится код assert False. Он бросит исключение AssertionError и номер строки, в которой произошла ошибка. 
Если код написан правильно и работал ранее, то такой результат равносилен тому, что наш автотест обнаружил баг в тестируемом веб-приложении. 
Если результат проверки вернет True, то выполнится выражение assert True. 
В этом случае код завершится без ошибок — тест прошел успешно. """