"""
Runtime: 32 ms, faster than 48.67% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 14.3 MB, less than 62.36% of Python3 online submissions for Minimum Genetic Mutation.
"""

import collections
from typing import List


class Solution:

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if end not in bank:
            return -1

        def distance(str1, str2, l=8) -> int:

            return sum([str1[i] != str2[i] for i in range(l)])

        candidates = collections.deque()

        candidates.append([start])

        while candidates:

            steps = candidates.popleft()

            prev = steps[-1]

            diff = distance(prev, end)

            if diff <= 1:
                return len(steps) - 1 + diff

            for nxt in bank:

                # print(nxt, prev, steps)
                if nxt not in steps and distance(nxt, prev) == 1:
                    candidates.append(steps + [nxt])

        return -1
















