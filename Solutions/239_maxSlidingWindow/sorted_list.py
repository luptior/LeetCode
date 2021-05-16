"""
Runtime: 6172 ms, faster than 5.01% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 29.7 MB, less than 83.50% of Python3 online submissions for Sliding Window Maximum.
"""

from bisect import bisect
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        tmp = sorted(nums[:k])

        result.append(tmp[-1])

        for i in range(1, len(nums) - k + 1):
            tmp.pop(bisect.bisect_left(tmp, nums[i - 1]))
            bisect.insort(tmp, nums[i + k - 1])

            result.append(tmp[-1])

        return result

