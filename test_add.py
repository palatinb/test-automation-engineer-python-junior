import pytest

import calculator


class TestAddClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,b,expected",
                             [(10, 5, 15),
                              (-1, 1, 0),
                              (-1, -1, -2)])
    def test_add(self, a, b, expected):
        assert self.calc.add(a, b) == expected

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
