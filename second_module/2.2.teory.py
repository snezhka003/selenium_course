# Шаг 2.2.2
""" Варианты ответа задаются тегом option, значение value может отсутствовать. 
Можно отмечать варианты с помощью обычного метода click(). 
Для этого сначала нужно применить метод click() для элемента с тегом select, чтобы список раскрылся, 
а затем кликнуть на нужный вариант ответа: """
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click() # эта строка может выглядеть и так: browser.find_element(By.CSS_SELECTOR, "[value='1']").click()


# Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver. 
from selenium.webdriver.support.ui import Select # импортируем класс из библиотеки
# Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select.
select = Select(browser.find_element(By.TAG_NAME, "select"))
# Далее можно найти любой вариант из списка с помощью метода select_by_value(value):
select.select_by_value("1") # ищем элемент с текстом "Python"

""" Можно использовать еще два метода: 
1. select.select_by_visible_text("text") - ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.
2. select.select_by_index(index) - ищет элемент по его индексу или порядковому номеру. 
Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1), 
так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--". """

# Шаг 2.2.4
""" С помощью метода execute_script можно выполнить программу, написанную на языке JavaScript, как часть сценария автотеста в запущенном браузере.
Давайте попробуем вызвать alert в браузере с помощью WebDriver. Пример сценария: """
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
""" исполняемый JavaScript нужно заключать в кавычки (двойные или одинарные). 
Если внутри скрипта вам также понадобится использовать кавычки, 
а для выделения скрипта вы уже используете двойные кавычки, то в скрипте следует поставить одинарные (или наоборот): """
browser.execute_script("document.title='Script executing';") # или так: browser.execute_script('document.title="Script executing";')
# либо применить экранирование внутренних двойных кавычек обратным слэшем \
browser.execute_script("alert(\"Robots at work\");")

""" Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой. 
Изменим сначала заголовок страницы, а затем вызовем alert: """
browser.execute_script("document.title='Script executing';alert('Robots at work');")

# Шаг 2.2.5
""" Для клика в WebDriver мы используем метод click(). 
Если элемент оказывается перекрыт другим элементом, то наша программа """
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()

""" вызовет следующую ошибку:
selenium.common.exceptions.WebDriverException: Message: unknown error: Element <button type="submit" 
class="btn btn-default" style="margin-bottom: 1000px;">...</button> is not clickable at point (87, 420). 
Other element would receive the click: <p>...</p> """

""" мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
Делается это с помощью следующего скрипта: "return arguments[0].scrollIntoView(true);"
Мы дополнительно передали в метод scrollIntoView аргумент true, чтобы элемент после скролла оказался в области видимости. """

# В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
""" В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу. 
После выполнения кода элемент button должен оказаться в верхней части страницы.
Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. Эта команда проскроллит страницу на 100 пикселей вниз: """
browser.execute_script("window.scrollBy(0, 100);")

# можно написать короче, без использования JS:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
_ = button.location_once_scrolled_into_view
button.click()
time.sleep(10)
browser.quit()

# Шаг 2.2.7
""" Если понадобится загрузить файл на веб-странице, можем использовать знакомый метод send_keys. 
Только теперь нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.
Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — os. 
В этом случае ваш код не будет зависеть от операционной системы, которую вы используете.
Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт, который вы запускаете: """
import os 

browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

""" Попробуйте добавить в файл отдельно команды print(os.path.abspath(__file__)) и 
print(os.path.abspath(os.path.dirname(__file__))) и посмотрите на разницу.
В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'. 
Фишка в том, что если мы файлы lesson2_step7.py вместе с file.txt перенесем в другую папку, 
или на компьютер с другой ОС, то такой код без правок заработает и там.
Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file". 
Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path)."""
"""
Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:

1. вбить руками
element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

2. задать с помощью переменных
# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)

3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)
"""

# итоговый код
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print(os.path.abspath(os.path.dirname(__file__)))

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

time.sleep(10)

browser.quit()
