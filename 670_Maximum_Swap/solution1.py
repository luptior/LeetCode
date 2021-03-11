"""
Runtime: 32 ms, faster than 61.10% of Python3 online submissions for Maximum Swap.
Memory Usage: 14.1 MB, less than 95.46% of Python3 online submissions for Maximum Swap.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:

        l = [int(x) for x in list(str(num))]

        n = len(l)

        maxi = -1
        best = None

        for i in range(n - 1):
            for j in range(i + 1, n):
                if l[i] >= l[j]:
                    continue

                print(i, j)

                imp = (10 ** (n - j) * l[i] + 10 ** (n - i) * l[j]) - (10 ** (n - i) * l[i] + 10 ** (n - j) * l[j])

                print(imp)

                if imp > maxi:
                    maxi = imp
                    best = (i, j)

        if not best:
            return num

        i, j = best

        l[i], l[j] = l[j], l[i]

        return int("".join([str(c) for c in l]))