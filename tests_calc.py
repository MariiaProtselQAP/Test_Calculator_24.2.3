import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 1, 2) == 2

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 2, 1) == 1
