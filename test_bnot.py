import pytest
import calculator
import binary_helper


class TestBitwiseNotClass:
    calc = calculator.Calculator()

    def test_bitwise_not(self):
        value_a = 156
        result = ""
        expected_result = self.calc.bnot(value_a)
        # Reversing the strings to start from the end
        binary_a, binary_b = binary_helper.convertToBinary(value_a)
        for i in range(len(binary_a)):
            if binary_a[i] == str(1):
                result += str(0)
            else:
                result += str(1)

        # After creating the result string I reverse it to convert it back to decimal
        actual_result = binary_helper.binaryToDecimal("".join(reversed(result)))

        assert expected_result == actual_result
        # Easier way to test the operator
        # assert self.calc.bnot(value_a) == ~value_a

    def test_bitwise_not_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bnot()