# Шаг 1.6.2
""" Для поиска элементов на странице в Selenium WebDriver используются несколько стратегий, 
позволяющих искать по атрибутам элементов, текстам в ссылках, CSS-селекторам и XPath-селекторам. 
Для поиска Selenium предоставляет метод find_element, который принимает два аргумента - тип локатора и значение локатора. 
Существуют следующие методы поиска элементов:

find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
find_element(By.NAME, value) — поиск по атрибуту name элемента;
find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.
Например, мы хотим найти кнопку со значением id="submit_button": """
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")

""" Вы можете столкнуться с ситуацией, когда на странице будет несколько элементов, подходящих под заданные вами параметры поиска. 
В этом случае WebDriver вернет вам только первый элемент, который встретит во время поиска по HTML. 
Если вам нужен не первый, а второй или следующие элементы, вам нужно либо задать более точный селектор для поиска, либо использовать методы find_elements """

# Шаг 1.6.3
""" обратите внимание на то, что необходимо явно закрывать окно браузера в нашем коде при помощи команды browser.quit(). 
Каждый раз при открытии браузера browser = webdriver.Chrome() в системе создается процесс, который останется висеть, 
если вы вручную закроете окно браузера. Чтобы не остаться без оперативной памяти после запуска нескольких скриптов, 
всегда добавляйте к своим скриптам команду закрытия: """
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()
# # закрываем браузер после всех манипуляций
browser.quit()

""" Важно еще пояснить разницу между двумя командами: browser.close() и browser.quit():
- browser.close() закрывает текущее окно браузера. Это значит, что если ваш скрипт вызвал всплывающее окно, 
или открыл что-то в новом окне или вкладке браузера, то закроется только текущее окно, а все остальные останутся висеть. 
- browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии. 
Всегда используйте browser.quit(). """ 

# Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, проще всего использовать конструкцию try/finally: 
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# Шаг 1.6.5
# попробуем искать элементы по тексту ссылки, для этого воспользуемся методом find_element_by_link_text:
link = browser.find_element(By.LINK_TEXT, 'text')

""" В качестве аргумента в метод передается такой текст, ссылку с которым мы хотим найти. 
Это тот самый текст, который содержится между открывающим и закрывающим тегом <a> вот тут </a>
Допустим, на странице https://www.degreesymbol.net/ мы хотим найти ссылку с текстом "Degree symbol in Math" 
и перейти по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код: """
link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link.click()

# А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код: 
link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()
# Обычно поиск по подстроке чуть более удобный и гибкий, но с ним надо быть вдвойне аккуратными и проверять, что находится нужный элемент.

# Шаг 1.6.6
""" метод find_element возвращает только первый из всех элементов, которые подходят под условия поиска. 
Иногда возникает ситуация, когда у нас есть несколько одинаковых по сути объектов на странице, 
например, иконки товаров в корзине интернет-магазина. 
В тесте нам нужно проверить, что отображаются все выбранные для покупки товары. 
Для этого существует метод find_elements, которые в отличие от find_element вернёт список 
всех найденных элементов по заданному условию. Проверив длину списка, мы можем удостовериться, 
что в корзине отобразилось правильное количество товаров. 
Пример кода (код приведен только для примера, сайта fake-shop.com скорее всего не существует): """
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    # подготовка для теста
    # открываем страницу первого товара
    # данный сайт не существует, этот код приведен только для примера
    browser.get("https://www.ozon.ru/product/korzina-dlya-belya-branq-zebra-uglovaya-tsvet-goluboy-40-l-137213328/?sh=HNs8dDvVkA")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, "._4-a1")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://www.ozon.ru/product/osteregaytes-poddelok-old-spise-original-3-sht-h-50-ml-dezodorant-stik-tverdyy-gelevyy-komplekt-iz-728647986/?sh=HNs8dFaU8g")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, "._4-a1")
    add_button.click()

    # тестовый сценарий
    # открываем корзину
    browser.get("https://www.ozon.ru/cart")

    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, ".c8b")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

""" !Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements. 
Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, 
которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат: 
если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде. """