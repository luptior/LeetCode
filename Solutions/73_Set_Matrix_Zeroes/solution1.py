"""
Runtime: 116 ms, faster than 99.12% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 15.2 MB, less than 44.16% of Python3 online submissions for Set Matrix Zeroes.

"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        c, r = set(), set()

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                r.add(i)
                for j, d in enumerate(matrix[i]):
                    if d == 0:
                        c.add(j)

        for row in r:
            matrix[row] = [0] * len(matrix[0])

        for column in c:
            for i in range(len(matrix)):
                matrix[i][column] = 0

