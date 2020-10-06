from math import ceil


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        count = 0

        for n in range(1, ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1):
            s = n * (n + 1) // 2

            if (N - s) % n == 0:
                count += 1

        return count