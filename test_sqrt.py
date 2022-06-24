import pytest
import calculator


class TestSqrtClass:
    calc = calculator.Calculator()

    def test_sqrt(self):
        assert self.calc.sqrt(9) == 3

    def test_sqrt_with_zero(self):
        assert self.calc.sqrt(0) == 0

    def test_sqrt_with_negative(self):
        with pytest.raises(ValueError):
            self.calc.sqrt(-1)

    def test_sqrt_with_empty_call(self):
        with pytest.raises(TypeError):
            self.calc.sqrt("")
