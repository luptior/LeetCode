"""
Runtime: 168 ms, faster than 81.98% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
Memory Usage: 18.2 MB, less than 41.28% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
"""

import bisect
import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):

        self.rects = rects
        self.weights = [(x[2] - x[0] + 1) * (x[3] - x[1] + 1) for x in rects]
        tmp_sum = sum(self.weights)
        for i, d in enumerate(self.weights):
            if i != 0:
                self.weights[i] = d / tmp_sum + self.weights[i - 1]
            else:
                self.weights[i] = d / tmp_sum

    def pick(self) -> List[int]:

        r = random.random()
        idx = bisect.bisect(self.weights, r)

        rect = self.rects[idx]

        return [random.choice(range(rect[0], rect[2] + 1)), random.choice(range(rect[1], rect[3] + 1))]