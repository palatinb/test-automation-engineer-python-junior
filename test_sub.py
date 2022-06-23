import pytest
import calculator


class TestSubClass:
    calc = calculator.Calculator()

    def test_sub(self):
        assert self.calc.sub(3, 5) == -2

    def test_sub_with_one_negative(self):
        assert self.calc.sub(-5, 5) == -10

    def test_sub_with_two_negative(self):
        assert self.calc.sub(-5, -5) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')
