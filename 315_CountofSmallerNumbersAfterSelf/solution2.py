
# left to right, still

from collections import deque

class Solution:
    def countSmaller(self, nums: [int]) -> [int]:

        result = []
        mem = {}

        for i in range(len(nums) - 1, -1, -1):
            count = [v for k, v in mem.items() if k < nums[i]]
            result.append(sum(count))
            if nums[i] in mem:
                mem[nums[i]] += 1
            else:
                mem[nums[i]] = 1

        return reversed(result)