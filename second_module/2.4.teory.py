# Шаг 2.4.3
""" один простой тест на WebDriver, проверяющий работу кнопки.
Тестовый сценарий выглядит так:
1. Открыть страницу http://suninjuly.github.io/wait1.html
2. Нажать на кнопку "Verify"
3. Проверить, что появилась надпись "Verification was successful!"
Для открытия страницы мы используем метод get, 
затем находим нужную кнопку с помощью одного из методов find_element_by_ 
и нажимаем на нее с помощью метода click. 
Далее находим новый элемент с текстом и проверяем соответствие текста на странице ожидаемому тексту.
Вот как выглядит код автотеста: """
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text

""" Если сначала выполнить тест вручную, а затем запустить автотест: 
В первом случае, вы завершите тест успешно, 
во втором случае автотест упадет с сообщением NoSuchElementException для элемента c id="verify".
Это происходит, потому что команды в Python выполняются синхронно, то есть, строго последовательно. 
Пока не завершится команда get, не начнется поиск кнопки. 
Пока кнопка не найдена, не будет сделан клик по кнопке и так далее. """

# Шаг 2.4.4
""" Теперь, когда мы уже знаем, что кнопка появляется с задержкой, мы можем добавить паузу до начала поиска элемента. 
Мы уже использовали библиотеку time ранее. Давайте применим ее и сейчас: """
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
time.sleep(1)
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text
browser.quit()

# Шаг 2.4.5
""" решение с time.sleep() плохое: оно не масштабируемое и трудно поддерживаемое.
Идеальное решение могло бы быть таким: нам всё равно надо избежать ложного падения тестов 
из-за асинхронной работы скриптов или задержек от сервера, 
поэтому мы будем ждать появление элемента на странице в течение заданного количества времени (например, 5 секунд). 
Проверять наличие элемента будем каждые 500 мс. Как только элемент будет найден, мы сразу перейдем к следующему шагу в тесте. 
Таким образом, мы сможем получить нужный элемент в идеальном случае сразу, в худшем случае за 5 секунд.
В Selenium WebDriver есть специальный способ организации такого ожидания, 
который позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам. 
Ожидание называется неявным (Implicit wait), так как его не надо явно указывать каждый раз, 
когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды.
Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep() и добавить одну строчку с методом implicitly wait: """
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text
browser.quit()
""" На каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице прежде, 
чем выбросить исключение NoSuchElementException. """

# Шаг 2.4.6
""" Во время поиска WebDriver каждые 0.5 секунды проверяет, появился ли нужный элемент в DOM-модели браузера 
(Document Object Model — «объектная модель документа», интерфейс для доступа к HTML-содержимому сайта). 
Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):

- Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
- Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. 
Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. 
Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
- Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), 
и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.

Знание причин появления исключений помогает отлаживать тесты и понимать, где находится баг в случае его возникновения.

Коротко о том, как запомнить кто есть кто:

- NoSuchElementException - нет такого вообще
- StaleElementReferenceException -  был элемент да сплыл
- ElementNotVisibleException - видишь элемент? И я не вижу, а он есть. """

# Шаг 2.4.7
""" мы решили проблему с ожиданием элементов на странице. 
Однако методы find_element проверяют только то, что элемент появился на странице. 
В то же время элемент может иметь дополнительные свойства, которые могут быть важны для наших тестов. 
Рассмотрим пример с кнопкой, которая отправляет данные:
- Кнопка может быть неактивной, то есть её нельзя кликнуть;
- Кнопка может содержать текст, который меняется в зависимости от действий пользователя. 
Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
- Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.
Если мы хотим в тесте кликнуть на кнопку, а она в этот момент неактивна, 
то WebDriver все равно проэмулирует действие нажатия на кнопку, но данные не будут отправлены.
попробуем запустить следующий тест: """
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()
""" WebDriver смог найти кнопку с id="verify" и кликнуть по ней, но тест упал на поиске элемента "verify_message" с итоговым сообщением:
no such element: Unable to locate element: {"method":"id","selector":"verify_message"}
Это произошло из-за того, что WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной. 
На странице мы специально задали программно паузу в 1 секунду после загрузки сайта перед активированием кнопки, 
но неактивная кнопка в момент загрузки — обычное дело для реального сайта.
Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться, когда кнопка станет кликабельной. 
Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных ожиданий (Explicit Waits), 
которые позволяют задать специальное ожидание для конкретного элемента. 
Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions. 
Улучшим наш тест: """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()
""" element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
Обратите внимание, что в объекте WebDriverWait используется функция until, 
в которую передается правило ожидания, элемент, а также значение, по которому мы будем искать элемент. 
В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:
- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present

Если мы захотим проверять, что кнопка становится неактивной после отправки данных, 
то можно задать негативное правило с помощью метода until_not: """
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

""" Решил побаловаться тем, что уже прошел на этом курсе: 
ставлю свою версию скрипта, который автоматом полученный ответ 
со страниц заданий отправляет на stepik в форму заполнения ответа: """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert
import time
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

def send_answer(answer, lessonURL):
    browser = webdriver.Chrome()
    email = '****@***.***' ## Mail to log in with
    password = '************' ## Password

    browser.get(lessonURL)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/course/575/promo?auth=login']")))
    current_url = str(browser.current_url)
    browser.find_element(By.XPATH, "//a[@href='/course/575/promo?auth=login']").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[ name = "login"]')))
    browser.find_element(By.CSS_SELECTOR, '[ name = "login"]').send_keys(email)
    browser.find_element(By.CSS_SELECTOR, '[name = "password"]').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
    time.sleep(2) ## Так и не понял почему, но без time.sleep метод get отказывается работать
    browser.get(lessonURL)
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']" )))
    browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']").clear()
    browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']").send_keys(answer)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class ="submit-submission"]' )))
    browser.find_element(By.CSS_SELECTOR, 'button[class ="submit-submission"]')
    # Всё это дело вызываю в конце каждого задания, сохраняя ответ в answer и указывая ручками ссылку на урок - lessonURL в файле с уроком
    # Код выше работает только для заданий, которые ещё не были выполнены - поленился добавить эту фичу, 
    # поэтому на сделанных уже заданиях будете получать InvalidElementStateException. 
    # Для проверки можно самому нажать на странице "Выполнить ещё раз" и прогнать этот код
    # https://github.com/VitaliyYa/sendToStepik - хороший вариант!