class Solution:
    def missingNumber(self, nums: [int]) -> int:

        for i in range(len(nums)+1):
            if i not in nums:
                return i



if __name__ == '__main__':
    example = [3,0,1]

    s = Solution()

    print(s.missingNumber(example))