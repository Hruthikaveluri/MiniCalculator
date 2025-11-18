# tests/automation/test_calculator_automation.py
import pytest
from app import calculator

# -------------------------------
#  AUTOMATION TESTING EXAMPLES
# -------------------------------

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, 5, 15)
])
def test_add_automation(a, b, expected):
    """Automated data-driven test for add()"""
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (0, 5, -5),
    (-5, -5, 0)
])
def test_subtract_automation(a, b, expected):
    """Automated data-driven test for subtract()"""
    assert calculator.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (0, 10, 0),
    (-2, 5, -10),
    (2, -2, -4)
])
def test_multiply_automation(a, b, expected):
    """Automated data-driven test for multiply()"""
    assert calculator.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-8, -2, 4),
    (0, 5, 0)
])
def test_divide_automation(a, b, expected):
    """Automated data-driven test for divide()"""
    assert calculator.divide(a, b) == expected


def test_divide_by_zero_automation():
    """Automated test to ensure division by zero raises ValueError"""
    with pytest.raises(ValueError):
        calculator.divide(5, 0)
