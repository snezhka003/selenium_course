# шаг 3.6.2

""" Conftest.py — конфигурация тестов

Ранее мы добавили фикстуру browser, которая создает нам экземпляр браузера для тестов в данном файле. 
Когда файлов с тестами становится больше одного, приходится в каждом файле с тестами описывать данную фикстуру. 
Это очень неудобно. Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py, 
который должен лежать в директории верхнего уровня в вашем проекте с тестами. 
Можно создавать дополнительные файлы conftest.py в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.

Создадим файл conftest.py в корневом каталоге нашего тестового проекта и перенесем туда фикстуру browser. 
Заметьте, насколько лаконичнее стал выглядеть файл с тестами - test_conftest.py.
Теперь, сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстуре browser. Фикстура передается в тестовый метод в качестве аргумента. 
Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.

ОЧЕНЬ ВАЖНО! 
Есть одна важная особенность поведения конфигурационных файлов, о которой вы обязательно должны знать. 
PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами. 
Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите, чтобы не возникало ситуации, когда вы запускаете тесты из папки tests:

tests/
├── conftest.py
├── subfolder
│   └── conftest.py
│   └── test_abs.py

следует избегать!

В таком случае применяются ОБА файла conftest.py, что может вести к непредсказуемым ошибкам и конфликтам.  

Таким образом можно переопределять разные фикстуры, но мы в рамках курса рекомендуем придерживаться одного файла 
на проект/задачу и держать их горизонтально, как-нибудь так: 

selenium_course_solutions/
├── section3
│   └── conftest.py
│   └── test_languages.py
├── section4 
│   └── conftest.py
│   └── test_main_page.py

правильно!

Будьте внимательны и следите, чтобы не было разных conftest во вложенных друг в друга директориях """

# шаг 3.6.3

""" Параметризация тестов

PyTest позволяет запустить один и тот же тест с разными входными параметрами. 
Для этого используется декоратор @pytest.mark.parametrize(). Наш сайт доступен для разных языков. 
Напишем тест, который проверит, что для сайта с русским и английским языком будет отображаться ссылка на форму логина - test_fixture7.py. 
Передадим в наш тест ссылки на русскую и английскую версию главной страницы сайта.

В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра. 
В самом тесте наш параметр тоже нужно передавать в качестве аргумента. 
Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов теста кавычки не нужны.
Запустите тест: pytest -s -v test_fixture7.py
Вы увидите, что запустятся два теста.  В названии каждого теста в квадратных скобках будет написан параметр, с которым он был запущен. 
Таким образом мы можем быстро и без дублирования кода увеличить количество проверок для похожих сценариев:

collected 2 items

test_fixture7.py::test_guest_should_see_login_link[ru]
start browser for test..

DevTools listening on ws://127.0.0.1:53941/devtools/browser/60e9212f-3606-4270-93f5-cb2b7bdd125d
PASSED
quit browser..

test_fixture7.py::test_guest_should_see_login_link[en-gb] 
start browser for test..

DevTools listening on ws://127.0.0.1:53961/devtools/browser/0d048c15-cda9-464b-b23f-d4d7a9a809d6
PASSED
quit browser..
=========== PASSES =============
======= short test summary info ===========
PASSED test_fixture7.py::test_guest_should_see_login_link[ru]
PASSED test_fixture7.py::test_guest_should_see_login_link[en-gb]
============ 2 passed in 10.57s ================

Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились с заданными параметрами. 
В таком случае отметка о параметризации должна быть перед объявлением класса:  """

# шаг 3.6.4

""" Для тех кто хочет не палить логины и пароли.

1) Создаем json файл с допустим с названием config.json
и ложим в него содержимое в таком виде:
{
  "login_stepik": "test@gmail.com",
  "password_stepik": "test"
}

2) импортируем библиотеку и создаем фикстуру:

import json
@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

3) Затем не забываем его результат передать в тестируемую функцию таким же образом как вы передаете состояние других фикстур таких как браузер и.т.д. 
т.к вызываемая функция у меня называется load_config, его имя я и передаю: а затем уже результат этих переменных используете там где считаете нужным:

class TestLogin:
    def test_authorization(self, browser, wait, load_config):

        login = load_config['login_stepik']
        password = load_config['password_stepik']

4) Для того чтобы при выгрузке данных в git не выгружался этот файл с ключами создаем текстовый файл .gitignore 
(обратите внимание на точку, и также необходимо удалить txt расширение в конце) 
и добавляем в него название нашего файла с расширением который нужно игнорировать в моем случае добавляю строку: config.json """