"""
Runtime: 32 ms, faster than 43.12% of Python3 online submissions for Longest Absolute File Path.
Memory Usage: 14.5 MB, less than 8.38% of Python3 online submissions for Longest Absolute File Path.
"""

class Solution:
    def lengthLongestPath(self, input: str) -> int:

        dir_list = input.split("\n")

        # print(dir_list)

        prev = []
        maxi = 0

        for i, dir in enumerate(dir_list):

            level = 0
            while "\t" in dir:
                level += 1
                dir = dir[1:]

            dir = "/" + dir if level >= 1 else dir
            if level > len(prev) or not prev:
                prev.append(dir)
            elif level <= len(prev):
                prev = prev[:level]
                prev.append(dir)

            if "." not in dir:
                continue
            maxi = max(maxi, sum([len(x) for x in prev]))

            # print(prev, level, maxi)

        return maxi
