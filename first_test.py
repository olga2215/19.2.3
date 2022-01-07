import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 77, 3) == 231

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 81, 9) == 9

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 7, 3) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 3) == 5