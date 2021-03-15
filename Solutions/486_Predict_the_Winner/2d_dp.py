"""

recursive + mem

Runtime: 36 ms, faster than 68.56% of Python3 online submissions for Predict the Winner.
Memory Usage: 14.3 MB, less than 57.08% of Python3 online submissions for Predict the Winner.

"""
class Solution:

    def __init__(self):
        self.mem = {}

    def PredictTheWinner(self, nums: [int]) -> bool:

        return self.getMax(nums, 0, len(nums) - 1) >= 0

    def getMax(self, nums, l, r):

        if l == r: return nums[l]

        if (l, r) in self.mem:
            return self.mem[(l, r)]

        result = max(nums[l] - self.getMax(nums, l + 1, r), nums[r] - self.getMax(nums, l, r - 1))
        self.mem[(l, r)] = result

        return result