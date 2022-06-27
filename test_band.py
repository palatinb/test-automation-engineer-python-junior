import pytest
import calculator
import binary_helper


class TestBitwiseAndClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a,b",
                             [(156, 52),
                              (351, 21),
                              (159, 65)])
    def test_bitwise_and(self, a, b):
        result = ""
        expected_result = self.calc.band(a, b)
        # Reversing the strings to start from the end
        binary_a, binary_b = binary_helper.convertToBinary(a, b)
        for i in range(len(binary_a)):
            if binary_a[i] == str(1) and binary_b[i] == str(1):
                result += str(1)
            else:
                result += str(0)

        # After creating the result string I reverse it to convert it back to decimal
        actual_result = binary_helper.binaryToDecimal("".join(reversed(result)))
        assert expected_result == actual_result
        # Easier way to test the operator
        # assert value_a & value_b == self.calc.band(value_a, value_b)

    def test_bitwise_and_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.band(156)
