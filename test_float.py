import pytest

"""
Кейс: погрешности при сложении float
"""
def test_float_fault_calc():
    assert 0.2 + 0.2 + 0.2 != 0.6


"""
Негативный кейс: операция получения количества элемента не определена
для float
"""
def test_float_get_length():
    with pytest.raises(TypeError):
        len(0.5)


"""
Параметризированный тест: проверка является ли число отрицательным
первые три теста - проверки на целочисленных значениях и граничном значении 0
следующие два - проверка дробных чисел
последние два - проверка очень маленького пограничного дробного значения и очень большого дробного
"""
@pytest.mark.parametrize("numb,expected",
                         [(-1, True),
                          (0, False),
                          (2, False),
                          (0.99, False),
                          (-0.00000000001, True),
                          (9999999999999.001, False)])
def test_float_is_negative(numb, expected):
    assert (numb < 0) == expected
