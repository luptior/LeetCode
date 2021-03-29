"""
Runtime: 88 ms, faster than 21.70% of Python3 online submissions for Insert Interval.
Memory Usage: 17.4 MB, less than 91.67% of Python3 online submissions for Insert Interval.
"""


from bisect import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        # return merged or empty if no overlap
        overlap = lambda x, y: max(x[0], y[0]) <= min(x[1], y[1]) # O(1)
        merge = lambda x, y: [min(x[0], y[0]), max(x[1], y[1])] # O(1)

        merge_id = []

        for i, interval in enumerate(intervals):  # O(N)

            if overlap(interval, newInterval) > 0:
                merge_id.append(i)

        if not merge_id:
            intervals.insert(bisect.bisect(intervals, newInterval), newInterval) # O(log(N))
            return intervals

        mini = merge_id[0]  # insert place

        for _ in range(len(merge_id)): # O(N)
            newInterval = merge(newInterval, intervals.pop(mini))

        intervals.insert(mini, newInterval)

        return intervals