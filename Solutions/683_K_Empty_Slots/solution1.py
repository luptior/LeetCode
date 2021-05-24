import bisect
from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:

        ranges = [[1, len(bulbs)]]  # initial range

        for i, bulb in enumerate(bulbs):

            idx = bisect.bisect_left([x[0] for x in ranges], bulb)
            if idx >= len(ranges):
                idx = -1

            if idx > 0 and bulb <= ranges[idx-1][1]:
                idx -= 1

            print("search:", ranges, bulb, idx)

            curr_range = ranges[idx]

            if bulb == curr_range[0]:
                ranges[idx][0] += 1

            elif bulb == curr_range[1]:
                ranges[idx][1] -= 1

            else:
                ranges.pop(idx)
                ranges.insert(idx, [bulb + 1, curr_range[1]])
                ranges.insert(idx, [curr_range[0], bulb - 1])

            print(i + 1, bulb, ranges)

            if ranges[idx][1] == len(bulbs) or idx + 1 < len(ranges) and ranges[idx + 1][1] == len(
                    bulbs):  # right end not closed
                continue

            if ranges[idx][0] == 1:  # left end not closed
                continue

            if ranges[idx][1] - ranges[idx][0] == k - 1 or idx + 1 < len(ranges) and ranges[idx + 1][1] - \
                    ranges[idx + 1][0] == k - 1:
                return i + 1

        return -1


if __name__ == '__main__':

    s = Solution()
    bulbs = [6,5,8,9,7,1,10,2,3,4]
    k = 2
    print(s.kEmptySlots(bulbs, k))



