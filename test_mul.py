import pytest
import calculator


class TestMulClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,b,expected",
                             [(10, 5, 50),
                              (2535, 0, 0),
                              (12, -3, -36),
                              (-35, -22, 770)])
    def test_multiple(self, a, b, expected):
        assert self.calc.mul(a, b) == expected

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
