from collections import deque

import math
class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:

        if k == 1: return nums

        