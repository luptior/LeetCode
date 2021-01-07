class Solution:
    def missingNumber(self, nums: [int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()