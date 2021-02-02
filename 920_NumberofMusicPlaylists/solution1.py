from functools import reduce
from math import factorial
from collections import Counter


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        return self.count_perm(list(range(N)))

    def count_perm(self, l: list):
        num = factorial(len(l))
        mults = Counter(l).values()

        den = reduce(operator.mul, (factorial(v) for v in mults), 1)

        return num // den