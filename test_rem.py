import math
import pytest

import calculator


class TestRemClass:
    calc = calculator.Calculator()

    def test_rem_with_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(24, 0)

    def test_rem(self):
        assert self.calc.rem(13, 5) == 3

    def test_rem_with_one_negative(self):
        assert self.calc.rem(-13, 5) == -13 - (math.floor((-13 / 5)) * 5)

    def test_rem_with_two_negative(self):
        assert self.calc.rem(-35, -5) == -35 - math.floor(-35 / -5) * -5

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
