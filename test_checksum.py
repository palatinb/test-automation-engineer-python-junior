import hashlib
import math
import sys
import pytest
import calculator


class TestChecksumClass:
    calc = calculator.Calculator()

    def test_checksum(self):
        assert str(self.calc.checksum(521)) == hashlib.md5(str(521).encode('utf-8')).hexdigest()

    def test_bitwise_and_with_missing_arg(self):
        with pytest.raises(TypeError):
            self.calc.checksum()
