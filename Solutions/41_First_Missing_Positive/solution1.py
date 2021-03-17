"""
Runtime: 36 ms, faster than 66.86% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.2 MB, less than 50.47% of Python3 online submissions for First Missing Positive.
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        maxi = max(nums)  # O(N)

        if maxi > 1:
            nSet = set(nums)

            for num in range(1, maxi):  # O(N)
                if num not in nSet:  # O(1)
                    return num
        elif maxi <= 0:
            return 1
        else:
            return 2

        return maxi + 1