import math
import sys
import pytest
import calculator


class TestSumClass:
    calc = calculator.Calculator()

    def test_Sum(self):
        assert self.calc.add(3, 5) == 8

    def test_SumOneNegative(self):
        assert self.calc.add(-5, 5) == 0

    def test_SumTwoNegative(self):
        assert self.calc.add(-5, -5) == -10

    def test_TypeError(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')

    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


class TestSubClass:
    calc = calculator.Calculator()

    def test_Sub(self):
        assert self.calc.sub(3, 5) == -2

    def test_SubOneNegative(self):
        assert self.calc.sub(-5, 5) == -10

    def test_SubTwoNegative(self):
        assert self.calc.sub(-5, -5) == 0

    def test_TypeError(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')


class TestMulClass:
    calc = calculator.Calculator()

    def test_MultipleWithZero(self):
        assert self.calc.mul(213213, 0) == 0

    def test_Multiple(self):
        assert  self.calc.mul(12, 22) == 264

    def test_MultipleOneNegative(self):
        assert  self.calc.mul(12, -3) == -36

    def test_MultipleTwoNegative(self):
        assert  self.calc.mul(-35, -22) == 770

    def test_TypeError(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')


class TestDivClass:
    calc = calculator.Calculator()

    def test_DivisionWithZero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(213213, 0) == 0

    def test_Division(self):
        assert  self.calc.div(5555, 5) == 1111

    def test_DivisionOneNegative(self):
        assert  self.calc.div(-54, 9) == -6

    def test_DivisionTwoNegative(self):
        assert  self.calc.div(-35, -5) == 7

    def test_DivisionPart(self):
        assert self.calc.div(10, 4) == 2.5

    def test_TypeError(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')


class TestRemClass:
    calc = calculator.Calculator()

    def test_RemWithZero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(24, 0) == 0

    def test_Rem(self):
        assert  self.calc.rem(13, 5) == 3

    def test_RemOneNegative(self):
        assert  self.calc.rem(-13, 5) == -13 - (math.floor((-13/5)) * 5)

    def test_RemTwoNegative(self):
        assert  self.calc.rem(-35, -5) == -35 - math.floor(-35/-5) * -5

    def test_TypeError(self):
        with pytest.raises(TypeError):
            self.calc.add(3, '6')


class TestSqrtClass:
    calc = calculator.Calculator()


class TestChecksumClass:
    calc = calculator.Calculator()


class TestBandClass:
    calc = calculator.Calculator()


class TestBorClass:
    calc = calculator.Calculator()


class TestBxorClass:
    calc = calculator.Calculator()


class TestBnotClass:
    calc = calculator.Calculator()


class TestBshlClass:
    calc = calculator.Calculator()


class TestBshrClass:
    calc = calculator.Calculator()
