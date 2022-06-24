import pytest
import calculator


class TestBitwiseShiftLeftClass:
    calc = calculator.Calculator()

    def test_bitwise_shift_left(self):
        value_a = 39
        shift = 2
        expected_result = self.calc.bshl(value_a, shift)
        assert expected_result == value_a * pow(2, shift)

    def test_bitwise_shift_left_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bshl(156)
