
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:

        n = len(nums)

        if n < 3:
            return []
        result = []

        for i in range(n-2):
            for j in range(i+1, n-1):

                a = nums[i]
                b = nums[j]
                c = 0 - a - b
                trio = sorted([a,b,c])

                if c in nums[j+1:] and trio not in result:
                    result.append(trio)

        return result


if __name__ == '__main__':

    s = Solution()

    nums = [-1, 0, 1, 2, -1, -4]

    print(s.threeSum(nums))


