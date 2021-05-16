"""
Runtime: 116 ms, faster than 85.94% of Python3 online submissions for Minimum Number of Refueling Stops.
Memory Usage: 14.6 MB, less than 38.75% of Python3 online submissions for Minimum Number of Refueling Stops.
"""

import heapq
from typing import List


class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        fuel = startFuel

        maxheap = []

        count = 0

        for location, add_fuel in stations:

            # print(location, add_fuel)

            if fuel > location:
                heapq.heappush(maxheap, -add_fuel)

            elif fuel == location:
                heapq.heappush(maxheap, -add_fuel)

                fuel += -heapq.heappop(maxheap)
                count += 1

            else:

                while fuel <= location:
                    if maxheap:
                        fuel += -heapq.heappop(maxheap)
                        count += 1
                    else:
                        return -1

                heapq.heappush(maxheap, -add_fuel)

            # print(fuel, maxheap)

        if fuel >= target:
            return count
        else:

            while fuel < target:

                if maxheap:
                    fuel += -heapq.heappop(maxheap)
                    count += 1
                else:
                    return -1

            return count





