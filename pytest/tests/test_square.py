import pytest

from src import shapes


@pytest.mark.parametrize("side_length, expected_area", [
    (5, 25),
    (4, 16),
    (6, 36),
])
def test_multiple_square_areas(side_length, expected_area):
    """
        Test the area calculation for multiple square shapes.

        This function uses the `pytest.mark.parametrize` decorator to run the test multiple times with different input values.

        Parameters:
        - `side_length` (int): The length of the side of the square shape.
        - `expected_area` (int): The expected area of the square shape.

        The function creates a `Square` object with the given `side_length` and then calls its `area()` method to calculate the actual area. It then asserts that the actual area is equal to the expected area.

        This function is used to test the `area()` method of the `Square` class in the `shapes` module.

        Returns:
        None
    """
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [
    (5, 20),
    (4, 16),
    (6, 24),
])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    """
        Test the perimeter calculation for multiple square shapes.

        This function takes two parameters:
        - `side_length`: The length of the side of the square shape.
        - `expected_perimeter`: The expected perimeter of the square shape.

        The function creates a `Square` object with the given `side_length` and then calls its `perimeter()` method to calculate the actual perimeter. It then asserts that the actual perimeter is equal to the expected perimeter.

        This function is used to test the `perimeter()` method of the `Square` class in the `shapes` module.

        Parameters:
        - `side_length` (int): The length of the side of the square shape.
        - `expected_perimeter` (int): The expected perimeter of the square shape.

        Returns:
        None
    """
    assert shapes.Square(side_length).perimeter() == expected_perimeter
