import math


def decimalToBinary(testVariable):
    # Write your code here

    if testVariable <= 1: return str(testVariable)
    curr = int(math.log2(testVariable))

    result = ["0"] * (curr + 1)

    result[0] = "1"

    ctr = 1
    left = testVariable - 2 ** curr

    if left == 0:
        return "".join(result)

    while left < 2 ** (curr - ctr):
        ctr += 1

    result[ctr:] = list(decimalToBinary(testVariable - 2 ** curr))

    return "".join(result)