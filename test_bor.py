import pytest
import binary_helper
import calculator


class TestBitwiseOrClass:
    calc = calculator.Calculator()
    binary = ""

    @pytest.mark.parametrize("a,b",
                             [(156, 52),
                              (351, 21),
                              (159, 65)])
    def test_bitwise_or(self, a, b):
        result = ""
        expected_result = self.calc.bor(a, b)
        # Reversing the strings to start from the end
        binary_a, binary_b = binary_helper.convertToBinary(a, b)

        for i in range(len(binary_a)):
            if binary_a[i] == str(0) and binary_b[i] == str(0):
                result += str(0)
            else:
                result += str(1)

        # After creating the result string I reverse it to convert it back to decimal
        actual_result = binary_helper.binaryToDecimal("".join(reversed(result)))
        assert expected_result == actual_result
        # Easier way to test the operator
        # assert value_a | value_b == self.calc.bor(value_a, value_b)

    def test_bitwise_or_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bor(156)
