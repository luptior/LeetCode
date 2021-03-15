# Runtime: 9608 ms, faster than 5.02% of Python3 online submissions for Frog Jump.
# Memory Usage: 21.8 MB, less than 24.25% of Python3 online submissions for Frog Jump.

class Solution:
    def canCross(self, stones: [int]) -> bool:

        mem = {}

        def next(k, stone_id):

            if True in mem.values():
                return True

            if stone_id == len(stones)-1:
                key = f"{k}_{len(stones)-1}"
                mem[key] = True
                return True

            if1, if2, if3 = False, False, False
            if k - 1 > 0 and stones[stone_id] + k - 1 in stones:
                key = f"{k-1}_{stones.index(stones[stone_id] + k - 1)}"
                if key in mem:
                    if1 = mem[key]
                else:
                    if1 = next(k-1, stones.index(stones[stone_id] + k - 1))
                    mem[key] = if1
            if k > 0 and stones[stone_id] + k in stones:
                key = f"{k}_{stones.index(stones[stone_id] + k)}"
                if key in mem:
                    if2 = mem[key]
                else:
                    if2 = next(k, stones.index(stones[stone_id] + k))
                    mem[key] = if2
            if stones[stone_id] + k + 1 in stones:
                key = f"{k+1}_{stones.index(stones[stone_id] + k+1)}"
                if key in mem:
                    if3 = mem[key]
                else:
                    if3 = next(k+1, stones.index(stones[stone_id] + k +1))
                    mem[key] = if3

            return if1 or if2 or if3

        return next(0, 0)



if __name__ == '__main__':
    s = Solution()

    print(s.canCross([0,1,3,5,6,8,12,17]))