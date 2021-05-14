"""
TLE
"""


import collections
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        def findWord(word):

            if m * n < len(word):
                return False

            seeds = collections.deque()

            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        seeds.append([(i, j)])

            def steps(i, j, prevs):

                result = []

                if i + 1 < m and (i + 1, j) not in prevs:
                    result.append((i + 1, j))

                if i - 1 >= 0 and (i - 1, j) not in prevs:
                    result.append((i - 1, j))

                if j - 1 >= 0 and (i, j - 1) not in prevs:
                    result.append((i, j - 1))

                if j + 1 < n and (i, j + 1) not in prevs:
                    result.append((i, j + 1))

                return result

            while seeds:

                # print(seeds)
                seed = seeds.popleft()  # list

                if len(seed) == len(word):
                    return True

                nxts = steps(seed[-1][0], seed[-1][1], seed)

                if not nxts:
                    continue

                for x in nxts:
                    if word[len(seed)] == board[x[0]][x[1]]:
                        seeds.appendleft(seed + [x])

            return False

        return [w for w in words if findWord(w)]