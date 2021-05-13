def printPascal(testVariable):
    # Write your code here
    if testVariable == 0:
        return [1]

    elif testVariable == 1:
        return [1, 1]

    else:
        tmp = printPascal(testVariable - 1)
        return [1] + [tmp[i] + tmp[i + 1] for i in range(testVariable - 1)] + [1]