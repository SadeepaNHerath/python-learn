import pytest

import src.shapes as shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(20, 10)


# Also able to use different class for the constant fixtures and use in any test


def test_area(rectangle):
    assert rectangle.area() == 10 * 20


def test_perimeter(rectangle):
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_eq(rectangle, weird_rectangle):
    assert rectangle != weird_rectangle
