"""
Runtime: 556 ms, faster than 53.01% of Python3 online submissions for Shortest Path to Get Food.
Memory Usage: 20.2 MB, less than 21.95% of Python3 online submissions for Shortest Path to Get Food.
"""

import collections
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        wl = collections.deque()

        start = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    start = [i, j]

        wl.append([*start, 0])
        visited = set()

        while wl:

            i, j, step = wl.popleft()

            if grid[i][j] == "#":
                return step
            elif (i, j) in visited or grid[i][j] == 'X':
                continue
            else:

                visited.add((i, j))
                if i + 1 < n:
                    wl.append([i + 1, j, step + 1])
                if j + 1 < m:
                    wl.append([i, j + 1, step + 1])
                if i - 1 >= 0:
                    wl.append([i - 1, j, step + 1])
                if j - 1 >= 0:
                    wl.append([i, j - 1, step + 1])

        return -1

