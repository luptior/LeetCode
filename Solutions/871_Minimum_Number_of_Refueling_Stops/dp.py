from typing import List


class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        dp = [startFuel] + [0] * len(stations)

        for i, (location, capacity) in enumerate(stations): # enumerate each fuel station

            print(i, (location, capacity) )

            for t in range(i, -1, -1): # enumerate so far how many stations have we used
                if dp[t] >= location: # if can reach the station, dp[t] is max distance previous step can reach
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity) # dp[t+1] is max distance this step can reach

                    print(" ", t, dp)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1


if __name__ == '__main__':
    s = Solution()

    print(s.minRefuelStops(150, 36,
                           [[7, 13], [10, 11], [12, 31], [22, 14], [32, 26], [38, 16], [50, 8], [54, 13],
                            [75, 4], [85, 2], [88, 35], [90, 9], [96, 35], [103, 16], [115, 33], [121, 6],
                            [123, 1], [138, 2], [139, 34]]))

