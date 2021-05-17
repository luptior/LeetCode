"""Runtime: 868 ms, faster than 75.76% of Python3 online submissions for Continuous Subarray Sum.
Memory Usage: 33.7 MB, less than 66.55% of Python3 online submissions for Continuous Subarray Sum.
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:


        sumi = 0
        d = {}
        d[0] =-1

        for i, num in enumerate(nums):
            sumi += num
            if k != 0:
                sumi = sumi % k

            if sumi in d:
                if i - d[sumi] > 1:
                    return True
            else:
                d[sumi] = i

            print(i, num, sumi, d)

        return False



if __name__ == '__main__':
    s = Solution()

    # assert s.checkSubarraySum(nums = [23,2,4,6,7], k = 6)
    # assert s.checkSubarraySum(nums = [23, 2, 6, 4, 7], k = 6)
    # assert not s.checkSubarraySum(nums = [23, 2, 6, 4, 7], k = 13)
    assert s.checkSubarraySum([23,2,4,6,6], 7)