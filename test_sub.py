import pytest
import calculator


class TestSubClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,b,expected",
                             [(10, 5, 5),
                              (-1, 1, -2),
                              (-1, -1, 0)])
    def test_sub(self, a, b, expected):
        assert self.calc.sub(a, b) == expected

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
