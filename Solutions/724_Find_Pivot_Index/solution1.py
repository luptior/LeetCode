# Runtime: 266 ms, faster than 39.48% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.3 MB, less than 48.88% of Python3 online submissions for Find Pivot Index.

class Solution:
    def pivotIndex(self, nums: [int]) -> int:

        left = 0
        right = sum(nums[1:])
        if left == right:
            return 0

        for i in range(1, len(nums)):

            left += nums[i - 1]
            if i <= len(nums):
                right -= nums[i]

            if left == right:
                return i

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([1,7,3,6,5,6]))