import numpy as np


def transpose(A: [[int]]) -> [[int]]:
    n = len(A)  # length

    for i in range(0, n - 1):
        for j in range(n // 2):
            print(i, j)
            A[0 + j][0 + i], A[0 + i][n - 1 - j], A[n - 1 - i][n - 1 - j], A[n - 1 - i][0 + j] = \
                A[0 + i][n - 1 - j], A[n - 1 - i][n - 1 - j], A[n - 1 - i][0 + j], A[0 + j][0 + i]

    return A


if __name__ == '__main__':

    s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Input:\n", np.asarray(s))
    s = transpose(s)
    print("Input:\n" , np.asarray(s))
