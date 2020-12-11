# simple DFS, will return TLE for sure

class Solution:
    def canCross(self, stones: [int]) -> bool:

        def next(k, stone_id):

            if stone_id == len(stones)-1:
                # print(k, stone_id, len(stones) - 1)
                return True

            if1, if2, if3 = False, False, False
            if k - 1 > 0 and stones[stone_id] + k - 1 in stones:
                if1 = next(k-1, stones.index(stones[stone_id] + k - 1))
            if k > 0 and stones[stone_id] + k in stones:
                if2 = next(k, stones.index(stones[stone_id] + k))
            if stones[stone_id] + k + 1 in stones:
                if3 = next(k+1, stones.index(stones[stone_id] + k +1))

            return if1 or if2 or if3

        return next(0, 0)



if __name__ == '__main__':
    s = Solution()

    print(s.canCross([0,1,3,5,6,8,12,17]))