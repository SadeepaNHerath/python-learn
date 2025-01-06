import math
import pytest
import src.my_functions as my_functions

@pytest.mark.slow
def test_very_slow():
    assert math.isclose(my_functions.divide(1, "2"), 0.5)

@pytest.mark.skip(reason="This feature is not ready yet")
def test_not_yet_implemented():
    assert False

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero():
    assert my_functions.divide(1, 0)
