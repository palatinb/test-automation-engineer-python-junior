import pytest

import binary_helper
import calculator


class TestBitwiseXorClass:
    calc = calculator.Calculator()
    binary = ""

    def test_bitwise_xor(self):
        value_a = 156
        value_b = 52
        result = ""
        expected_result = self.calc.bxor(value_a, value_b)
        # Reversing the strings to start from the end
        binary_a, binary_b = binary_helper.convertToBinary(value_a, value_b)

        for i in range(len(binary_a)):
            if (binary_a[i] == str(1) and binary_b[i] == str(0)) or (binary_a[i] == str(0) and binary_b[i] == str(1)):
                result += str(1)
            else:
                result += str(0)

        # After creating the result string I reverse it to convert it back to decimal
        actual_result = binary_helper.binaryToDecimal("".join(reversed(result)))
        assert expected_result == actual_result
        # Easier way to test the operator
        # assert value_a ^ value_b == self.calc.bxor(value_a, value_b)

    def test_bitwise_xor_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bxor(156)