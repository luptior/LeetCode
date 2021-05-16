"""

Approach 2: Dynamic Programming, Kadane's Algorithm
"""

class Solution:
    def maxSubArray(self, nums: [int]) -> int:

        if len(nums) == 1:
            return nums[0]

        maxi = nums[0]
        current = nums[0]

        for n in nums[1:]:

            current = max(n, current + n) # current is the current array max

            maxi = max(maxi, current)

        return maxi






if __name__ == '__main__':
    example = nums = [-2,1,-3,4,-1,2,1,-5,4]

    s = Solution()

    assert s.maxSubArray(example) == 6