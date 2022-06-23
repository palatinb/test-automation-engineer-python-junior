import pytest

import calculator


class TestDivClass:
    calc = calculator.Calculator()

    def test_division_with_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(213213, 0)

    def test_division(self):
        assert self.calc.div(5555, 5) == 1111

    def test_division_with_one_negative(self):
        assert self.calc.div(-54, 9) == -6

    def test_division_with_two_negative(self):
        assert self.calc.div(-35, -5) == 7

    def test_division_part(self):
        assert self.calc.div(10, 4) == 2.5

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
