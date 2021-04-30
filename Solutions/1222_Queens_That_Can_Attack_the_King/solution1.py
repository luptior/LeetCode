from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        vertical = lambda x, y: y == king[1]
        horizontal = lambda x, y: x == king[0]

        b = king[1] - king[0]
        up = lambda x, y: y - x == b

        c = king[1] + king[0]
        down = lambda x, y: y + x == c

        sets = [[]] * 8

        for queen in queens:

            if vertical(*queen):
                if queen[0] > king[0]:
                    sets[0] = [min(queen[0], sets[0][0]), queen[1]] if sets[0] else queen
                else:
                    sets[1] = [max(queen[0], sets[1][0]), queen[1]] if sets[1] else queen

            elif horizontal(*queen):
                if queen[1] > king[1]:
                    sets[2] = [queen[0], min(queen[1], sets[2][1])] if sets[2] else queen
                else:
                    sets[3] = [queen[0], max(queen[1], sets[3][1])] if sets[3] else queen

            elif up(*queen):
                if queen[0] > king[0]:
                    sets[4] = [min(queen[0], sets[4][0]), min(queen[1], sets[4][1])] if sets[4] else queen
                else:
                    sets[5] = [max(queen[0], sets[5][0]), max(queen[1], sets[5][1])] if sets[5] else queen

            elif down(*queen):

                if queen[0] > king[0]:
                    sets[6] = [min(queen[0], sets[6][0]), max(queen[1], sets[6][1])] if sets[6] else queen
                else:
                    sets[7] = [max(queen[0], sets[7][0]), min(queen[1], sets[7][1])] if sets[7] else queen

        sets = [s for s in sets if s]

        return sets