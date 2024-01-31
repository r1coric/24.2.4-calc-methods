import pytest

from venv.calc import calculator


class TestCalc:
    def setup(self):
        self.calc = TestCalc

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

