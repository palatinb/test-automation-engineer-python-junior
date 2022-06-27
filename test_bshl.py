import pytest
import calculator


class TestBitwiseShiftLeftClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,shift",
                             [(156, 2),
                              (354, 3),
                              (159, 1)])
    def test_bitwise_shift_left(self, a, shift):
        expected_result = self.calc.bshl(a, shift)
        assert expected_result == a * pow(2, shift)

    def test_bitwise_shift_left_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bshl(156)
