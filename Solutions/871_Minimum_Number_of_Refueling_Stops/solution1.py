"""TLE solution"""


from functools import lru_cache
from typing import List


class Solution:
    def __init__(self):

        self.mini = None

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        stations.sort(key=lambda x: x[0])

        if startFuel >= target:
            return 0

        if not stations:
            return -1

        self.mini = len(stations) + 1

        def step(location, fuel, idx, num_stations):

            print(location, fuel, idx, num_stations)

            if num_stations >= self.mini:  # no need to explore
                return

            if fuel < 0:  # no fuel
                return

            if idx < len(stations) and location + fuel < stations[idx][0]:  # cannot reach next stop
                return

            if location + fuel >= target:  # can reach dest
                self.mini = min(num_stations, self.mini)
                return
            else:
                if idx == len(stations):
                    # reaches the end
                    return

            step(stations[idx][0], fuel - (stations[idx][0] - location) + stations[idx][1], idx + 1, num_stations + 1)
            step(stations[idx][0], fuel - (stations[idx][0] - location), idx + 1, num_stations)

        step(0, startFuel, 0, 0)

        return self.mini if self.mini != len(stations) + 1 else -1


if __name__ == '__main__':
    s = Solution()

    print(s.minRefuelStops(1000, 36,
                           [[7, 13], [10, 11], [12, 31], [22, 14], [32, 26], [38, 16], [50, 8], [54, 13],
                            [75, 4], [85, 2], [88, 35], [90, 9], [96, 35], [103, 16], [115, 33], [121, 6],
                            [123, 1], [138, 2], [139, 34], [145, 30], [149, 14], [160, 21], [167, 14], [188, 7],
                            [196, 27], [248, 4], [256, 35], [262, 16], [264, 12], [283, 23], [297, 15], [307, 25],
                            [311, 35], [316, 6], [345, 30], [348, 2], [354, 21], [360, 10], [362, 28], [363, 29],
                            [367, 7], [370, 13], [402, 6], [410, 32], [447, 20], [453, 13], [454, 27], [468, 1],
                            [470, 8], [471, 11], [474, 34], [486, 13], [490, 16], [495, 10], [527, 9], [533, 14],
                            [553, 36], [554, 23], [605, 5], [630, 17], [635, 30], [640, 31], [646, 9], [647, 12],
                            [659, 5], [664, 34], [667, 35], [676, 6], [690, 19], [709, 10], [721, 28], [734, 2],
                            [742, 6], [772, 22], [777, 32], [778, 36], [794, 7], [812, 24], [813, 33], [815, 14],
                            [816, 21], [824, 17], [826, 3], [838, 14], [840, 8], [853, 29], [863, 18], [867, 1],
                            [881, 27], [886, 27], [894, 26], [917, 3], [953, 6], [956, 3], [957, 28], [962, 33],
                            [967, 35], [972, 34], [984, 8], [987, 12]]))
