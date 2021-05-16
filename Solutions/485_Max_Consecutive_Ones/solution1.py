from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

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

        return max(candidates) if candidates else 0
