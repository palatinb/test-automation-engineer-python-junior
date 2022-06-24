import pytest

import calculator


class TestAddClass:
    calc = calculator.Calculator()

    def test_add(self):
        assert self.calc.add(3, 5) == 8

    def test_add_with_one_negative(self):
        assert self.calc.add(-5, 5) == 0

    def test_add_with_two_negative(self):
        assert self.calc.add(-5, -5) == -10

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
