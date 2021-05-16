"""
Runtime: 508 ms, faster than 33.31% of Python3 online submissions for Sliding Window Median.
Memory Usage: 15.9 MB, less than 65.86% of Python3 online submissions for Sliding Window Median.
"""

from bisect import bisect
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        result = []

        def median(l):
            if len(l) % 2 == 1:
                return l[len(l) // 2]
            else:
                return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

        tmp = sorted(nums[:k])

        result.append(median(tmp))

        for i in range(1, len(nums) - k + 1):
            tmp.pop(bisect.bisect_left(tmp, nums[i - 1]))
            bisect.insort(tmp, nums[i + k - 1])

            result.append(median(tmp))

        return result




