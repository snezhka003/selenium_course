""" дан шаблон для функции test_substring, которая принимает два значения: full_string и substring. 

Функция должна проверить вхождение строки substring в строку full_string 
с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. """ 

substring = "some_value"
full_string = "fulltext"
""" def test_substring(full_string, substring): """
assert substring in full_string, \
    f"expected '{substring}' to be substring of '{full_string}'"