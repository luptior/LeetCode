# dfs + memorization

class Solution:

    def __init__(self):
        self.mem = {}

    def canJump(self, nums: [int]) -> bool:

        return self.jump(0, nums)

    def jump(self, idx: int, partial_nums : [int]) -> bool:


        if idx in self.mem:
            return self.mem[idx]

        if len(partial_nums) == 1:
            self.mem[idx] = True
            return True

        if partial_nums[0] == 0:
            self.mem[idx] = False
            return False

        result = False
        for x in range(1, partial_nums[0]):
            if x <= len(partial_nums):
                if idx + x in self.mem:
                    result = result or self.mem[idx + x ]
                else:
                    result = result or self.jump(idx + x, partial_nums[x:])

        self.mem[idx] = result
        return result


if __name__ == '__main__':
    s = Solution()

    test = [2,3,1,1,4]

    print(s.canJump(test))