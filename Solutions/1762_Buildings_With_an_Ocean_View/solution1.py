"""
Runtime: 772 ms, faster than 100.00% of Python3 online submissions for Buildings With an Ocean View.
Memory Usage: 31.4 MB, less than 100.00% of Python3 online submissions for Buildings With an Ocean View.
"""
import collections
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        if not heights:
            return []

        if len(heights) == 1:
            return [0]

        result = []

        max_from_right = collections.deque([heights[-1]])
        result.append(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_from_right[0]:
                result.append(i)
            max_from_right.appendleft(max(heights[i], max_from_right[0]))

        return list(reversed(result))
