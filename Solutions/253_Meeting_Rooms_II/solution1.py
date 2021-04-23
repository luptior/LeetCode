import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        room = []

        heapq.heappush(room, intervals[0][1])  # end time

        for interval in intervals[1:]:

            if room[0] <= interval[0]:
                heapq.heappop(room)

            heapq.heappush(room, interval[1])

        return len(room)