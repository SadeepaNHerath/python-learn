import math

import src.my_functions as my_functions


def test_add():
    assert my_functions.add(1, 2) == 3


def test_add_string():
    assert my_functions.add("1", "2") == 3


def test_add_mixed():
    assert my_functions.add(1, "2") == 3


def test_add_invalid():
    assert my_functions.add(1, "two") == 1


def test_divide():
    assert math.isclose(my_functions.divide(1, 2), 0.5)


def test_divide_string():
    assert math.isclose(my_functions.divide("1", "2"), 0.5)


def test_divide_mixed():
    assert math.isclose(my_functions.divide(1, "2"), 0.5)


def test_divide_invalid():
    assert my_functions.divide(1, "two") == "Error: Invalid input. Please provide numbers."


def test_divide_zero():
    assert my_functions.divide(1, 0) == "Error: Division by zero is not allowed."
