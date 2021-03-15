# bfs + memorization,
# Runtime: 6492 ms, faster than 5.22% of Python3 online submissions for Shortest Path to Get All Keys.
# Memory Usage: 33.2 MB, less than 5.39% of Python3 online submissions for Shortest Path to Get All Keys.

from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: [str]) -> int:

        m = len(grid)
        n = len(grid[0])

        start =[0,0]
        all_keys = []

        for i, row in enumerate(grid):
            if "@" in row:
                start = [i, row.index("@")]

            for c in row:
                if c.islower():
                    all_keys.append(c)

        all_keys = set(all_keys)
        print(all_keys)

        wl = deque([[start[0], start[1], 0, []]]) # x, y, steps, keys

        visited = {}


        while wl:
            x, y, steps, keys = wl.popleft()

            if (x,y) not in visited:
                visited[(x, y)] = [steps, keys]
            else:
                prev_steps, prev_keys = visited[(x, y)]
                if set(keys).issubset(set(prev_keys)) and steps >= prev_steps:
                    continue
                visited[(x, y)] = [steps, keys]

            if len(all_keys - set(keys)) == 0:
                return steps-1

            val = grid[x][y]

            if val == ".":
                if x + 1 < m:
                    wl.append([x+1, y, steps+1, keys])
                if y + 1 < n:
                    wl.append([x, y+1, steps + 1, keys])
                if y -1 >= 0:
                    wl.append([x, y-1, steps + 1, keys])
                if x - 1 >= 0:
                    wl.append([x -1, y, steps + 1, keys])

            elif val.islower():
                if val in keys:
                    if x + 1 < m:
                        wl.append([x + 1, y, steps + 1, keys])
                    if y + 1 < n:
                        wl.append([x, y + 1, steps + 1, keys])
                    if y - 1 >= 0:
                        wl.append([x, y - 1, steps + 1, keys])
                    if x - 1 >= 0:
                        wl.append([x - 1, y, steps + 1, keys])
                else:
                    if x + 1 < m:
                        wl.append([x + 1, y, steps + 1, keys+[val]])
                    if y + 1 < n:
                        wl.append([x, y + 1, steps + 1, keys+[val]])
                    if y - 1 >= 0:
                        wl.append([x, y - 1, steps + 1, keys+[val]])
                    if x - 1 >= 0:
                        wl.append([x - 1, y, steps + 1, keys+[val]])

            elif val.isupper():
                if val.lower() not in keys:
                    # no suitable keys, stop here
                    continue
                else:
                    if x + 1 < m:
                        wl.append([x + 1, y, steps + 1, keys])
                    if y + 1 < n:
                        wl.append([x, y + 1, steps + 1, keys])
                    if y - 1 >= 0:
                        wl.append([x, y - 1, steps + 1, keys])
                    if x - 1 >= 0:
                        wl.append([x - 1, y, steps + 1, keys])

            elif val == "@":
                if x + 1 < m:
                    wl.append([x + 1, y, steps + 1, keys])
                if y + 1 < n:
                    wl.append([x, y + 1, steps + 1, keys])
                if y - 1 >= 0:
                    wl.append([x, y - 1, steps + 1, keys])
                if x - 1 >= 0:
                    wl.append([x - 1, y, steps + 1, keys])

            else:
                continue

            # print(x, y, steps, keys, wl)

        return -1


if __name__ == '__main__':

    s = Solution()
    # i = ["@.a.#","###.#","b.A.B"]

    i =["@abcdeABCDEFf"]
    import numpy as np

    new_i = [ list(x) for x in i]
    n = np.asarray(new_i, dtype=str)

    print(n)

    print(s.shortestPathAllKeys(i))