# Шаг 2.3.2
""" рассмотрим ситуацию, когда в сценарии теста возникает необходимость не только получить содержимое alert, 
но и нажать кнопку OK, чтобы закрыть alert. Alert является модальным окном: 
это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. 
Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept(): """
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
alert = browser.switch_to.alert
alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

""" Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm. 
Для переключения на окно confirm используется та же команда, что и в случае с alert: """
confirm = browser.switch_to.alert
confirm.accept()
# Для confirm-окон можно использовать следующий метод для отказа:
confirm.dismiss() # То же самое, что и при нажатии пользователем кнопки "Отмена". 

""" Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. 
Чтобы ввести текст, используйте метод send_keys(): """
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

# Шаг 2.3.5
""" WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать со старой вкладкой. 
Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window: """
browser.switch_to.window(browser.window_handles[1])
""" Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. 
Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку: """
new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
first_window = browser.window_handles[0]
# Текущую вкладку можно узнать так:
current_window = browser.current_window_handle

# window_handles возвращает list
windows = browser.window_handles
current_window = browser.current_window_handle

for win in windows:
    if current_window == win:
        print(win, " with current index: ", windows.index(win))
    else:
        print(win, " with index: ", windows.index(win))