"""
Runtime: 368 ms, faster than 82.66% of Python3 online submissions for Max Consecutive Ones II.
Memory Usage: 14.4 MB, less than 50.95% of Python3 online submissions for Max Consecutive Ones II.

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not 0 in nums:
            return len(nums)

        candidates = []

        prev = 0

        for n in nums:

            if n == 1:
                if prev == 0:
                    candidates.append(1)
                else:
                    candidates[-1] += 1
                prev = 1
            else:
                prev = 0
                candidates.append(0)

        # O(N) so far

        if candidates and sum(candidates) == 0:
            return 1

        maxi = 0

        for i, candidate in enumerate(candidates):

            if candidate > 0:
                maxi = max(maxi, (candidates[i - 2] if i - 2 >= 0 else 0) + (1 if i - 1 >= 0 else 0) + candidate,
                           candidate + (candidates[i + 2] if i + 2 < len(candidates) else 0) + (
                               1 if i + 1 < len(candidates) else 0))

        return maxi