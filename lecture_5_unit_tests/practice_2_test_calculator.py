import pytest

from practice_1_calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# Um die Funktion zu testen, muss "py -m pytest practice_2_test_calculator.py" im Terminal eingegeben werden.