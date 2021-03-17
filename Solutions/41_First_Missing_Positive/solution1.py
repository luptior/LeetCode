"""
Runtime: 32 ms, faster than 87.71% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.3 MB, less than 17.03% of Python3 online submissions for First Missing Positive.
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        maxi = max(nums)  # O(N)

        if maxi > 1:
            nSet = set([n for n in nums if n > 0])

            for num in range(1, len(nSet) + 1):  # O(N)
                if num not in nSet:  # O(1)
                    return num
        elif maxi <= 0:
            return 1
        else:
            return 2

        return maxi + 1