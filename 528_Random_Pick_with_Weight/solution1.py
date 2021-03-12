"""
Runtime: 164 ms, faster than 97.08% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 19 MB, less than 20.08% of Python3 online submissions for Random Pick with Weight.

"""
import bisect
from random import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        s = sum(w)

        self.w = w

        self.prop = [n / s for n in w]

        # print(self.prop)

        for i in range(1, len(self.prop)):
            self.prop[i] += self.prop[i - 1]

            # print(self.prop)

    def pickIndex(self) -> int:
        r = random()

        n = bisect.bisect_left(self.prop, r)

        return n