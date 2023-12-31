# шаг 3.4.2

""" Классические фикстуры (fixtures).

Важной составляющей в использовании PyTest является концепция фикстур. 
Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.

Назначение фикстур может быть самым разным. 
Одно из распространенных применений фикстур — это подготовка тестового окружения и очистка тестового 
окружения и данных после завершения теста. Но, вообще говоря, фикстуры можно использовать для самых разных целей: 
для подключения к базе данных, с которой работают тесты, 
создания тестовых файлов или подготовки данных в текущем окружении с помощью API-методов.

Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами.

Можно создавать фикстуры для модулей, классов и отдельных функций.
Фикстуры включают в себя необязательный параметр под названием scope, который определяет, 
как часто фикстура получает setup и teardown. 
Параметр scope для @pytest.fixture(scope='function', autouse=False) может иметь значения 
функции, класса, модуля или сессии. Scope по умолчанию — это функция. 

Краткое описание каждого значения Scope:

- scope='function'
Выполняется один раз для каждой функции теста. Часть setup запускается перед каждым тестом с помощью fixture. 
Часть teardown запускается после каждого теста с использованием fixture. Это область используемая по умолчанию, если параметр scope не указан.

- scope='class'
Выполняется один раз для каждого тестового класса, независимо от количества тестовых методов в классе.

- scope='module'
Выполняется один раз для каждого модуля, независимо от того, сколько тестовых функций или методов или других фикстур при использовании модуля.

- scope='session'
Выполняется один раз за сеанс. Все методы и функции тестирования, использующие фикстуру области сеанса, используют один вызов setup и teardown.

Параметр autouse по умолчанию - это False , в этом случае фикстуру необходимо вызвать вручную. 
При autouse=True фикстура будет вызываться автоматически с периодичностью, указанной в параметре scope. Например:

@pytest.fixture(scope='module', autouse=True)
def print_text():
    print('Начало работы фикстуры')
    yield
    print('Завершение работы фикстуры')

- Фикстура без вызова запустится в начале модуля, 
- выведет сообщение о начале своей работы,
- передаст выполнение тестам,
- по завершению работы всего кода в модуле сообщит, что завершает работу. 

Давайте попробуем написать фикстуру для инициализации браузера, который мы затем сможем использовать в наших тестах. 
После окончания тестов мы будем автоматически закрывать браузер с помощью команды browser.quit(), 
чтобы в нашей системе не оказалось множество открытых окон браузера. 
Вынесем инициализацию и закрытие браузера в фикстуры, чтобы не писать этот код для каждого теста.

Будем сразу объединять наши тесты в тест-сьюты, роль тест-сьюта будут играть классы, в которых мы будем хранить наши тесты.

Рассмотрим два примера: создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта 
и создание браузера для каждого теста во втором тест-сьюте. 
Сохраните следующий код в файл test_fixture1.py и запустите его с помощью PyTest. 
Не забудьте указать параметр -s, чтобы увидеть текст, который выводится командой print():
pytest -s test_fixture1.py

В консоли видим:
collected 4 items

test_fixture1.py
start browser for test suite 1..

DevTools listening on ws://127.0.0.1:64404/devtools/browser/a337be93-4e9e-4df8-a1f8-41d8291f4291
start test link 1
.start test basket 1
.quit browser for test suite 1..
start browser for test 2..

DevTools listening on ws://127.0.0.1:64424/devtools/browser/c73d7a1c-62bf-406e-a75d-48dfa8d6486c
start test link 2
.quit browser for test 2..
start browser for test 2..

DevTools listening on ws://127.0.0.1:64445/devtools/browser/7a785780-cfe0-4555-904d-6f995e5a7505
start test basket 2
.quit browser for test 2..
=== 4 passed in 27.52s =====

Мы видим, что в первом тест-сьюте браузер запустился один раз, а во втором — два раза.

Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста, 
поэтому лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее. 
К тому же если вдруг браузер зависнет в одном тесте, то другие тесты не пострадают, если они запускаются каждый в собственном браузере.

Минусы запуска браузера на каждый тест: каждый запуск и закрытие браузера занимают время, 
поэтому тесты будут идти дольше. Возможно, вы захотите оптимизировать время прогона тестов, 
но лучше это делать с помощью других инструментов, которые мы разберём в дальнейшем.

Обычно такие фикстуры переезжают вместе с тестами, написанными с помощью unittest, 
и приходится их поддерживать, но сейчас все пишут более гибкие фикстуры @pytest.fixture, которые мы рассмотрим в следующем шаге.  """

# шаг 3.4.3

""" Фикстуры, возвращающие значение.

Мы рассмотрели базовый подход к созданию фикстур, когда тестовые данные задаются и очищаются в setup и teardown методах. 
PyTest предлагает продвинутый подход к фикстурам, когда фикстуры можно задавать глобально, 
передавать их в тестовые методы как параметры, а также имеет набор встроенных фикстур. 
Это более гибкий и удобный способ работы со вспомогательными функциями, и сейчас вы сами увидите почему. 

Возвращаемое значение

Фикстуры могут возвращать значение, которое затем можно использовать в тестах. 
Давайте перепишем наш предыдущий пример с использованием PyTest фикстур. 
Мы создадим фикстуру browser, которая будет создавать объект WebDriver. 
Этот объект мы сможем использовать в тестах для взаимодействия с браузером. 
Для этого мы напишем метод browser и укажем, что он является фикстурой с помощью декоратора @pytest.fixture. 
После этого мы можем вызывать фикстуру в тестах, передав ее как параметр. 
По умолчанию фикстура будет создаваться для каждого тестового метода, то есть для каждого теста запустится свой экземпляр браузера.
Запишем его в файл test_fixture2.py и запустим его с помощью PyTest: pytest -s -v test_fixture2.py """

# шаг 3.4.4

""" Финализаторы — закрываем браузер.

Вероятно, вы заметили, что мы не использовали в примере test_fixture2.py команду browser.quit(). 
Это привело к тому, что несколько окон браузера оставались открыты после окончания тестов, 
а закрылись только после завершения всех тестов. 
Закрытие браузеров произошло благодаря встроенной фикстуре — сборщику мусора. 
Но если бы количество тестов насчитывало больше нескольких десятков, 
то открытые окна браузеров могли привести к тому, что оперативная память закончилась бы очень быстро. 
Поэтому надо явно закрывать браузеры после каждого теста. Для этого мы можем воспользоваться финализаторами. 
Один из вариантов финализатора — использование ключевого слова Python: yield. 
После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом yield: test_fixture3.py 

Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры request и ее метода addfinalizer: test_fixture3_1.py. 

Рекомендуем также выносить очистку данных и памяти в фикстуру, вместо того чтобы писать это в шагах теста: финализатор выполнится даже в ситуации, когда тест упал с ошибкой. """

# шаг 3.4.5

""" Область видимости scope.

Для фикстур можно задавать область покрытия фикстур. 
Допустимые значения: “function”, “class”, “module”, “session”. 
Соответственно, фикстура будет вызываться один раз для тестового метода, 
один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии. 

Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class" в фикстуре browser: test_fixture5.py

Мы видим, что в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере. 
Здесь мы проделали это в качестве примера, но мы крайне рекомендуем всё же запускать 
отдельный экземпляр браузера для каждого теста, чтобы повысить стабильность тестов. 
Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это работа с базами данных), 
можно вызывать и один раз за сессию запуска тестов.

Используйте pytest -v --setup-show "путь"

Если добавить параметр --setup-show, то можно отследить список используемых фикстур в каждом тесте. """

# шаг 3.4.6

""" Автоиспользование фикстур.

При описании фикстуры можно указать дополнительный параметр autouse=True, 
который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова: test_fixture_autouse.py
В консоли:
collected 2 items

test_fixture_autouse.py::TestMainPage1::test_guest_should_see_login_link
preparing some critical data for every test

        SETUP    F prepare_data
start browser for test..

DevTools listening on ws://127.0.0.1:50481/devtools/browser/72683592-05dc-4843-90e3-80bcdbf0d36a

        SETUP    F browser
        test_fixture_autouse.py::TestMainPage1::test_guest_should_see_login_link (fixtures used: browser, prepare_data)PASSED
quit browser..

        TEARDOWN F browser
        TEARDOWN F prepare_data
test_fixture_autouse.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page
preparing some critical data for every test

        SETUP    F prepare_data
start browser for test..

DevTools listening on ws://127.0.0.1:50503/devtools/browser/d1aa6d77-0dc2-4298-b165-cbd56776df4e

        SETUP    F browser
        test_fixture_autouse.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page (fixtures used: browser, prepare_data)PASSED
quit browser..

        TEARDOWN F browser
        TEARDOWN F prepare_data
         
Видим, что для каждого теста фикстура подготовки данных выполнилась без явного вызова. 
Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов. 
Без явной необходимости автоиспользованием фикстур лучше не пользоваться. 

Итог.
Вспомогательные функции — это очень мощная штука, которая решает много проблем при работе с автотестами. 
Основной плюс в том, что их удобно использовать в любых тестах без дублирования лишнего кода. 

Дополнительные материалы про фикстуры, которые мы настоятельно советуем почитать, приведены ниже:
https://habr.com/ru/company/yandex/blog/242795/
https://docs.pytest.org/en/stable/fixture.html """