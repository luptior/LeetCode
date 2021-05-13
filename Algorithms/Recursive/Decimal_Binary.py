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


# better solution
def decimalToBinary2(testVariable):
    # Base Case
    if testVariable <= 1:
        return str(testVariable)

    # Recursive Case
    else:
        return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2)  # Floor division -
        # division that results into whole number adjusted to the left in the number line
