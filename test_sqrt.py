import pytest
import calculator


class TestSqrtClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,expected",
                             [(9, 3),
                              (0, 0),
                              (25, 5)])
    def test_sqrt(self, a, expected):
        assert self.calc.sqrt(a) == expected

    def test_sqrt_with_negative(self):
        with pytest.raises(ValueError):
            self.calc.sqrt(-1)

    def test_sqrt_with_empty_call(self):
        with pytest.raises(TypeError):
            self.calc.sqrt("")
