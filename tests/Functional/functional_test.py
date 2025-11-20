# tests/functional/test_calculator_functional.py
import pytest
from app import calculator

def test_complete_workflow():
    """Test full workflow of multiple operations."""
    # Step 1: Add two numbers
    result = calculator.add(10, 5)
    assert result == 15

    # # Step 2: Multiply the result by 2
    result = calculator.multiply(result, 2)
    assert result == 30

    # Step 3: Subtract 10
    result = calculator.subtract(result, 10)
    assert result == 20

    # Step 4: Divide by 5
    result = calculator.divide(result, 5)
    assert result == 4


def test_divide_by_zero_functional():
    """Test full workflow with division by zero in between operations."""
    with pytest.raises(ValueError) as exc_info:
        # Add → Subtract → Divide by zero
        result = calculator.add(8, 2)
        result = calculator.subtract(result, 5)
        result = calculator.divide(result, 0)
    assert "Cannot divide by zero" in str(exc_info.value)


def test_negative_number_operations():
    """Functional flow with negative numbers."""
    result = calculator.add(-3, -7)
    assert result == -10

    result = calculator.multiply(result, -2)
    assert result == 20

    result = calculator.divide(result, 4)
    assert result == 5


def test_sequential_operations():
    """Check if multiple sequential operations maintain accuracy."""
    numbers = [10, 5, 2]
    result = calculator.add(numbers[0], numbers[1])
    result = calculator.divide(result, numbers[2])
    result = calculator.multiply(result, 3)
    assert result == 22.5
