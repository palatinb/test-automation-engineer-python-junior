def decimalToBinary(n):
    """
    In case we would like do the convert from decimal to binary
    if n >= 1:
        self.decimalToBinary(n // 2)
    self.binary += n % 2
    """

    result = bin(n).replace("0b", "")
    return result


def binaryToDecimal(n):
    return int(n, 2)


def convertToBinary(*values):
    binary_a = "".join(reversed(decimalToBinary(values[0])))
    binary_b = ""
    length_a = len(binary_a)
    length_b = 0
    if len(values) > 1:
        binary_b = "".join(reversed(decimalToBinary(values[1])))
        length_b = len(binary_b)
        if length_a < length_b:
            for i in range(length_a, length_b):
                binary_a += str(0)
        else:
            for i in range(length_b, length_a):
                binary_b += str(0)

    return binary_a, binary_b
