"""

Solved by sorting

Runtime: 100 ms, faster than 20.89% of Python3 online submissions for Wiggle Sort.
Memory Usage: 15.3 MB, less than 18.59% of Python3 online submissions for Wiggle Sort.
"""

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = sorted(nums)

        # print(s)
        counter = 0

        while s:

            if counter > len(nums) - 1:
                counter = 1

            # print(counter, s, nums )

            nums[counter] = s.pop(0)

            counter += 2


