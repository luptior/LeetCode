"""

Time exceeded

"""


from collections import deque

class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:

        q = [[1], [-1]]

        for i in range(len(nums)-1):

            tmp = []
            for x in q:
                tmp.append(x + [-1,])
                tmp.append(x + [1, ])
            q = tmp[:]

        result = 0

        for candidate in q:
            if sum([ nums[i] * candidate[i] for i in range(len(nums))]) == S:
                # print(candidate)
                result += 1

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(s.findTargetSumWays(nums, S))