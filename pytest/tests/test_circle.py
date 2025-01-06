import math
import pytest
import src.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        self.circle = shapes.Circle(10)

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
