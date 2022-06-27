import pytest
import calculator


class TestBitwiseShiftRightClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,shift",
                             [(156, 2),
                              (354, 3),
                              (159, 1)])
    def test_bitwise_shift_right(self, a, shift):
        expected_result = self.calc.bshr(a, shift)
        actual_result = a // pow(2, shift)
        assert expected_result == actual_result

    def test_bitwise_shift_right_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bshr(156)
