import pytest

import calculator


class TestDivClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,b,expected",
                             [(5555, 5, 1111),
                              (-54, 9, -6),
                              (-35, -5, 7),
                              (10, 4, 2.5)])
    def test_division(self, a, b, expected):
        assert self.calc.div(a, b) == expected

    def test_division_with_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(213213, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
