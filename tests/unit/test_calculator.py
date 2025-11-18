import pytest
from app.calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(3, 2) == 5

def test_add_negative_numbers():
    assert add(-3, -2) == -5

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2



def test_divide_numbers():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
