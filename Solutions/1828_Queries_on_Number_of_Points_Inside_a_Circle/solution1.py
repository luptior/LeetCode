"""
Runtime: 3132 ms, faster than 18.26% of Python3 online submissions for Queries on Number of Points Inside a Circle.
Memory Usage: 14.6 MB, less than 80.16% of Python3 online submissions for Queries on Number of Points Inside a Circle.
"""

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        def inside(pt1, pt2, r):

            x1, y1 = pt1  # center
            x2, y2 = pt2  # query

            if (x1 - x2) ** 2 + (y1 - y2) ** 2 > r ** 2:
                return False
            else:
                return True

        result = []

        for q in queries:
            tmp = 0
            for pt in points:
                if inside(q[:2], pt, q[-1]):
                    tmp += 1
            result.append(tmp)

        return result
