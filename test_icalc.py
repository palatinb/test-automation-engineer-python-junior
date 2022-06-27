import icalc
import pytest


class TestIcalcClass:

    @pytest.mark.parametrize("test_input,expected", [("3 5", "8\n"), ("2 4", "6\n"), ("6 9", "15\n")])
    def test_interactive_mode_add(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_add(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("3 5", "-2\n"), ("12 5", "7\n"), ("6 -9", "15\n")])
    def test_interactive_mode_sub(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_sub(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("5555 5", "1111\n"), ("-54 9", "-6\n"), ("-35 -5", "7\n"), ("10 4", "2.5\n")])
    def test_interactive_mode_div(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_div(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("10 5", "50\n"), ("232 0", "0\n"), ("6 -9", "-54\n")])
    def test_interactive_mode_mul(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_mul(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("13 5", "3\n"), ("8 4", "0\n"), ("-35 -5", "0\n")])
    def test_interactive_mode_rem(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_rem(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("9", "3\n"), ("0", "0\n"), ("25", "5\n")])
    def test_interactive_mode_sqrt(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_sqrt(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("156 52", "168\n"), ("351 21", "330\n"), ("159 65", "222\n")])
    def test_interactive_mode_bxor(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_bit_xor(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("156 2", "39\n"), ("354 3", "44\n"), ("159 1", "79\n")])
    def test_interactive_mode_bshr(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_bit_shift_right(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("156 2", "624\n"), ("354 3", "2832\n"), ("159 1", "318\n")])
    def test_interactive_mode_bshl(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_bit_shift_left(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("156 52", "188\n"), ("351 21", "351\n"), ("159 65", "223\n")])
    def test_interactive_mode_bor(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_bit_or(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("156", "-157\n"), ("351", "-352\n"), ("159", "-160\n")])
    def test_interactive_mode_bnot(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_bit_not(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''

    @pytest.mark.parametrize("test_input,expected", [("156 52", "20\n"), ("351 21", "21\n"), ("159 65", "1\n")])
    def test_interactive_mode_band(self, capsys, test_input, expected):
        calc = icalc.InteractiveCalculator()

        calc.do_bit_and(test_input)
        out, err = capsys.readouterr()

        assert out == expected
        assert err == ''
