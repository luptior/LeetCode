"""
Runtime: 80 ms, faster than 5.62% of Python3 online submissions for Reveal Cards In Increasing Order.
Memory Usage: 14.3 MB, less than 81.16% of Python3 online submissions for Reveal Cards In Increasing Order.
"""


import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()

        idx = collections.deque(range(len(deck)))

        ordered_idx = []

        result = [0] * len(idx)

        while idx:

            ordered_idx.append(idx.popleft())  # 1
            if idx:
                idx.append(idx.popleft())

        for i in range(len(deck)):
            # print(deck[ordered_idx[i]])
            result[ordered_idx[i]] = deck[i]

        return result
