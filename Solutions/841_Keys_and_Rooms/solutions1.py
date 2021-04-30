"""
Runtime: 68 ms, faster than 41.10% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.8 MB, less than 57.14% of Python3 online submissions for Keys and Rooms.
"""

import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        wl = collections.deque([0])

        result = set([])

        while wl:
            node = wl.popleft()

            if node in result:
                continue

            result.add(node)

            for dest in rooms[node]:
                wl.append(dest)

        return len(rooms) == len(result)






