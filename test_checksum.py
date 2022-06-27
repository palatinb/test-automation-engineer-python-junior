import hashlib
import pytest
import calculator


class TestChecksumClass:
    calc = calculator.Calculator()

    @pytest.mark.parametrize("a",
                             [521,
                              354,
                              296])
    def test_checksum(self, a):
        assert str(self.calc.checksum(a)) == hashlib.md5(str(a).encode('utf-8')).hexdigest()

    def test_bitwise_and_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.checksum()
