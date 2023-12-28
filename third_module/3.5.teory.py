# шаг 3.5.2

""" Маркировка тестов часть 1.

Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям, 
но также по каким-нибудь заданным нами категориям. 
Например, мы можем выбрать небольшое количество критичных тестов (smoke), 
которые нужно запускать на каждый коммит разработчиков, 
а остальные тесты обозначить как регрессионные (regression) и запускать их только перед релизом. 
Или у нас могут быть тесты, специфичные для конкретного браузера (internet explorer 11), 
и мы хотим запускать эти тесты только под данный браузер. 
Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks). 
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка.

Давайте разделим тесты в одном из предыдущих примеров на smoke и regression: test_fixture8.py
Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку: pytest -s -v -m smoke test_fixture8.py, 
должен запуститься только тест с маркировкой smoke.
При этом вы увидите warning, то есть предупреждение:

PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, 
see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

Это предупреждение появилось потому, что в последних версиях PyTest настоятельно рекомендуется регистрировать метки явно перед использованием. 
Это, например, позволяет избегать опечаток, когда вы можете ошибочно пометить ваш тест несуществующей меткой, и он будет пропускаться при прогоне тестов.

Как же регистрировать метки?
Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests

Текст после знака ":" является поясняющим — его можно не писать.

Снова запустите тесты: pytest -s -v -m smoke test_fixture8.py
Теперь предупреждений быть не должно.

Так же можно маркировать целый тестовый класс. В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс. """

# шаг 3.5.3

""" Маркировка тестов часть 2.

Инверсия
Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. 
Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду: pytest -s -v -m "not smoke" test_fixture8.py

Объединение тестов с разными маркировками
Для запуска тестов с разными метками можно использовать логическое ИЛИ. 
Запустим smoke и regression-тесты: pytest -s -v -m "smoke or regression" test_fixture8.py

Выбор тестов, имеющих несколько маркировок
Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной операционной системы, 
например, для Windows 10. Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному из тестов эту метку: test_fixture81.py

Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И: pytest -s -v -m "smoke and win10" test_fixture81.py
Должен выполниться тест test_guest_should_see_basket_link_on_the_main_page.  """

# шаг 3.5.4

""" Пропуск тестов
В PyTest есть стандартные метки, которые позволяют пропустить тест при сборе тестов для запуска 
(то есть не запускать тест) или запустить, но отметить особенным статусом тот тест, 
который ожидаемо упадёт из-за наличия бага, чтобы он не влиял на результаты прогона всех тестов. 
Эти метки не требуют дополнительного объявления в pytest.ini.

Пропустить тест

Итак, чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip: test_3_5_4.py 
В результатах теста мы увидим, что один тест был пропущен, а другой успешно прошёл: "1 passed, 1 skipped"."""

# шаг 3.5.5

""" XFail: помечать тест как ожидаемо падающий.

Отметить тест как падающий

Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser): 
     browser.get(link)
     browser.find_element(By.CSS_SELECTOR, "button.favorite")

Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала. 
Пока разработчики исправляют баг, мы хотим, чтобы результат прогона всех наших тестов был успешен, 
но падающий тест помечался соответствующим образом, чтобы про него не забыть. 
Добавим маркировку @pytest.mark.xfail для падающего теста: test_fixture10.py
Запустим наши тесты: pytest -v test_fixture10.py
Наш упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный:
collected 3 items

test_fixture10.py::TestMainPage1::test_guest_should_see_login_link
DevTools listening on ws://127.0.0.1:55385/devtools/browser/52398167-bda7-4c45-8649-9053fb0efbad
PASSED                                                                                                                              [ 33%]
test_fixture10.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page 
DevTools listening on ws://127.0.0.1:55405/devtools/browser/7e497154-3fef-4043-b879-d2e236076a4e
PASSED                                                                                                            [ 66%]
test_fixture10.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page 
DevTools listening on ws://127.0.0.1:55425/devtools/browser/fc1df39a-6fde-46e7-aa19-31eae4198b10
XFAIL                                                                                                           [100%]
========== 2 passed, 1 xfailed in 15.42s ===========

Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит). 
После этого маркировку xfail для теста можно удалить. 
Кстати, к маркировке xfail можно добавлять параметр reason: test_fixture10a.py 
Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx: pytest -rx -v test_fixture10a.py

Сравните вывод в первом и во втором случае:
collected 3 items

test_fixture10a.py::TestMainPage1::test_guest_should_see_login_link
DevTools listening on ws://127.0.0.1:55469/devtools/browser/ce374290-32f4-4496-9dcf-dfb41f90de26
PASSED                                                                                                                             [ 33%]
test_fixture10a.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page 
DevTools listening on ws://127.0.0.1:55489/devtools/browser/7e381164-28c9-4e3c-850e-0b89c9d022f0
PASSED                                                                                                           [ 66%]
test_fixture10a.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page 
DevTools listening on ws://127.0.0.1:55509/devtools/browser/8cfeb59e-7dc1-46b9-8300-7ec3277cda32
XFAIL (fixing this bug right now)                                                                              [100%]
============= short test summary info =============
XFAIL test_fixture10a.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page
  fixing this bug right now
======= 2 passed, 1 xfailed in 15.52s ==========

XPASS-тесты

Поменяем селектор в последнем тесте, чтобы тест начал проходить: test_fixture10b.py
Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам: pytest -rX -v test_fixture10b.py
И изучите отчёт:
collected 3 items

test_fixture10b.py::TestMainPage1::test_guest_should_see_login_link
DevTools listening on ws://127.0.0.1:55544/devtools/browser/5e47826b-96ed-4e77-9810-b8f0af77eb11
PASSED                                                                                                                             [ 33%]
test_fixture10b.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page 
DevTools listening on ws://127.0.0.1:55564/devtools/browser/3fbebc0e-fdfc-4b29-a02d-5319472d8d32
PASSED                                                                                                           [ 66%]
test_fixture10b.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page 
DevTools listening on ws://127.0.0.1:55584/devtools/browser/5bf71c4b-4a9a-45bf-88a4-39ebf2940957
XPASS (fixing this bug right now)                                                                              [100%]
======== short test summary info =====================
XPASS test_fixture10b.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page fixing this bug right now
========== 2 passed, 1 xpassed in 16.00s ========  """

# шаг 3.5.7

""" нужно разобраться в хитросплетениях маркировок. 
Мы имеем файл с тестами, которые уже размечены маркерами для разных ситуаций запуска: test_task_run_1.py

Тесты № 1 и № 4 будут найдены и выполнены PyTest при запуске следующей команды: pytest -v -m "smoke and not beta_users" test_task_run_1.py """