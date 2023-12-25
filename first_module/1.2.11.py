import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
options = Options()
driver = webdriver.Chrome(options=options)

options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(10)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

""" Для того чтобы использовать свой, нужно ему его в качестве аргумента командной строки передать,
которая вот с помощью этой функции add_argument и передается. Для того чтобы изи узнать свой профайл, 
нужно сделать след.: ввести в используемом браузере chrome://version, там будет Profile Path - его нужно скопировать и передать в метод. 
ВАЖНЫЙ момент - нельзя запускать скрипт, если уже открыт браузер, иначе он просто его откроет и ничего делать не будет. 
Закрываем браузер, запускаем скрипт - все ок. Как открывать в новой вкладке запущенного браузера я разбираться не стал. 
В связи со всем вышесказанным, рабочий код будет выглядеть так: """
""" from selenium import webdriver
from selenium.webdriver.chrome.options import Options """


""" def main():
    zapustis_ti_uje_nakonec()


def zapustis_ti_uje_nakonec():
    try:
        chromedriver = 'C:\chromedriver\chromedriver.exe'
        chrome_options = Options()
        profile_path = 'path\to\profile'
        chrome_options.add_argument(f'user-data-dir={profile_path}')
        driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
        driver.get('http://google.com')
    finally:
        driver.quit()


if __name__ == '__main__':
    main() """