import pytest


# Негативный кейс: тюпл неизменяем
def test_tuple_assign():
    new_tuple = (100, 200, 300)
    with pytest.raises(TypeError):
        new_tuple[0] = 'new_value'


# Позитивный кейс: обмен значениями переменных через tuple
def test_tuple_swap():
    a = 1
    b = 2
    (b, a) = (a, b)
    assert b == 1 and a == 2


"""
 Параметризированный тест: проверка конвертации разных типов данных в tuple
 Проверяем конвертацию в tuple разных типов данных:
 Строки, списка из чисел, списка из строк
 Словарь разными типами ключей (число, строка)
"""


@pytest.mark.parametrize("for_convert,expected",
                         [
                             ('mail', ("m", "a", "i", "l")),
                             ([1, 2, 3], (1, 2, 3)),
                             (["один", "два", "три"], ("один", "два", "три")),
                             ({1: "one", 2: "two"}, (1, 2)),
                             ({"first": "1", "second": "2"}, ("first", "second"))
                         ])
def test_tuple_one(for_convert, expected):
    assert tuple(for_convert) == expected
