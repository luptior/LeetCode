"""
TLE

"""
import collections
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        wl = collections.deque()

        wl.append([amount, 0])

        while wl:

            curr, step = wl.popleft()

            # print(curr, step, wl)

            for c in coins[::-1]:

                if c < curr:

                    wl.append([curr - c, step + 1])

                elif c == curr:

                    return step + 1

        return -1


