import math
import pytest

import calculator


class TestRemClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,b,expected",
                             [(13, 5, 3),
                              (-13, 5, -13 - (math.floor((-13 / 5)) * 5)),
                              (-35, -5, -35 - math.floor(-35 / -5) * -5)])
    def test_rem(self, a, b, expected):
        assert self.calc.rem(a, b) == expected

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')

    def test_rem_with_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(24, 0)
