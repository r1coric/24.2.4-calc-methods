import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 56, 44) == 100

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self, 100,40) == 60

    def test_division_succes(self):
        assert self.calc.division(self, 100,10) == 10

    def test_multiply_succes(self):
        assert self.calc.multiply(self, 100,10) == 1000

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1,0)

