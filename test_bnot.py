import pytest
import calculator


class TestBitwiseNotClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a",
                             [156,
                              351,
                              159])
    def test_bitwise_not(self, a):
        assert self.calc.bnot(a) == -(a+1)

    def test_bitwise_not_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.bnot()
