class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        s = set(nums)

        l = len(s)

        nums[:l] = list(s)

        while len(nums) > l:
            nums.pop()

        nums.sort()