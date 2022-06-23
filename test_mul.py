import pytest
import calculator


class TestMulClass:
    calc = calculator.Calculator()

    def test_multiple_with_zero(self):
        assert self.calc.mul(213213, 0) == 0

    def test_multiple(self):
        assert self.calc.mul(12, 22) == 264

    def test_multiple_with_one_negative(self):
        assert self.calc.mul(12, -3) == -36

    def test_multiple_with_two_negative(self):
        assert self.calc.mul(-35, -22) == 770

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
