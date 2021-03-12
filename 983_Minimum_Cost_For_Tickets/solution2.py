from functools import lru_cache
from typing import List


class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dayset = set(days)

        durations = [1, 7, 30]

        @lru_cache(None)
        def step(i):

            if i > 365:
                return 0

            elif i in dayset:

                return min(step(i + d) + c for d, c in zip(durations, costs))

            else:
                return step(i + 1)

        return step(0)