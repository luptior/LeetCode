class Solution:
    def PredictTheWinner(self, nums: [int]) -> bool:
        return self.getMax(nums, 0, len(nums) - 1) >= 0

    def getMax(self, nums, l, r):
        if l == r: return nums[l]
        return max(nums[l] - self.getMax(nums, l + 1, r), nums[r] - self.getMax(nums, l, r - 1))