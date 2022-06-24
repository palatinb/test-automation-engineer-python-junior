import pytest
import calculator


class TestBitwiseShiftRightClass:
    calc = calculator.Calculator()

    def test_bitwise_shift_right(self):
        value_a = 157
        shift = 2
        expected_result = self.calc.bshr(value_a, shift)
        actual_result = value_a // pow(2, shift)
        assert expected_result == actual_result

    def test_bitwise_shift_right_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bshr(156)