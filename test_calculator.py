import pytest

from calculator import add, subtract, multiply, divide


def test_addition():
    assert add(5, 3) == 8


def test_subtraction():
    assert subtract(10, 4) == 6


def test_multiplication():
    assert multiply(6, 7) == 42


def test_division():
    assert divide(20, 4) == 5


def test_operations_with_negative_numbers():
    assert add(-5, 3) == -2
    assert subtract(-5, 3) == -8
    assert multiply(-5, 3) == -15
    assert divide(-6, 3) == -2


def test_operations_with_decimal_numbers():
    assert add(2.5, 1.5) == 4
    assert subtract(5.5, 2.5) == 3
    assert multiply(2.5, 2) == 5
    assert divide(7.5, 2.5) == 3


def test_division_by_zero():
    with pytest.raises(
        ZeroDivisionError,
        match="Division by zero is not allowed.",
    ):
        divide(10, 0)