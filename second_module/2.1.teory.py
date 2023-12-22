# Шаг 2.1.2
""" Checkbox (чекбокс или флажок) и radiobutton (радиобаттон или переключатель) — часто используемые в формах элементы.
Оба этих элемента создаются при помощи тега input со значением атрибута type равным checkbox или radio соответственно. 
В html-коде страницы вы увидите:
<input type="checkbox">
<input type="radio">

Если checkbox или radiobutton выбран, то у элемента появится новый атрибут checked без значения. 
Часто атрибут checked уже установлен для одного из элементов по умолчанию.
<input type="checkbox" checked>
<input type="radio" checked>

Radiobuttons объединяются в группу, где все элементы имеют одинаковые значения атрибута name, 
но разные значения атрибута value:
<input type="radio" name="language" value="python" checked>
<input type="radio" name="language" value="selenium">

Checkboxes могут иметь как одинаковые, так и разные значения атрибута name. 
Поэтому и те, и другие лучше искать с помощью значения id или значения атрибута value. 
Если вы видите на странице чекбокс с уникальным значением name, то можете искать по name.

Чтобы снять/поставить галочку в элементе типа checkbox или выбрать опцию из группы radiobuttons, 
надо указать WebDriver метод поиска элемента и выполнить для найденного элемента метод click(): """
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()

""" Также вы можете увидеть тег label рядом с input. Этот тег используется, чтобы сделать кликабельным текст, 
который отображается рядом с флажком. Этот текст заключен внутри тега label. 
Элемент label связывается с элементом input с помощью атрибута for, 
в котором указывается значение атрибута id для элемента input:

<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
<div>
  <input type="radio" id="java" name="language">
  <label for="java">Java</label>
</div>
В этом случае можно также отметить нужный пункт с помощью WebDriver, выполнив метод click() на элементе label. """
option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
option1.click()

# Шаг 2.1.5
""" Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. 
Обратите внимание, что скобки здесь не нужны: """
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, "input_value")
x = x_element.text
y = calc(x)
""" Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение". """

# Шаг 2.1.6
""" Для более детальных проверок в тесте нам может понадобиться узнать значение атрибута элемента. 
Атрибуты могут быть стандартными свойствами, которые понимает и использует браузер для отображения 
и вёрстки элементов или для хранения служебной информации, например, name, width, height, color и многие другие. 
Также атрибуты могут быть созданы разработчиками проекта для задания собственных стилей или правил.

Значение атрибута представляет собой строку. Если значение атрибута отсутствует, 
то это равносильно значению атрибута равному "false". 
Давайте еще раз взглянем на страницу http://suninjuly.github.io/math.html. 
На ней есть radiobuttons, для которых выбрано значение по умолчанию. 
В автотесте нам может понадобиться проверить, что для одного из radiobutton по умолчанию уже выбрано значение. 
Для этого мы можем проверить значение атрибута checked у этого элемента. Вот HTML-код элемента:
<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked> """

# Найдём этот элемент с помощью WebDriver:
people_radio = browser.find_element(By.ID, "peopleRule")

# Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
# Т.к. у данного атрибута значение не указано явно, то метод get_attribute вернёт "true".
# Мы можем написать проверку другим способом, сравнив строки:
assert people_checked == "true", "People radio is not selected by default"

""" Если атрибута нет, то метод get_attribute вернёт значение None. 
Применим метод get_attribute ко второму radiobutton, и убедимся, что атрибут отсутствует. """
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

""" Так же мы можем проверять наличие атрибута disabled, который определяет, 
может ли пользователь взаимодействовать с элементом. 
Например, в предыдущем задании на странице с капчей для роботов JavaScript 
устанавливает атрибут disabled у кнопки Submit, когда истекает время, отведенное на решение задачи.
<button type="submit" class="btn btn-default" disabled>Submit</button> """