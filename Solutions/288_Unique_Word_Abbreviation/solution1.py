"""
Runtime: 280 ms, faster than 5.07% of Python3 online submissions for Unique Word Abbreviation.
Memory Usage: 27.5 MB, less than 46.76% of Python3 online submissions for Unique Word Abbreviation.

"""


import collections
from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):

        self.d = collections.defaultdict(set)

        for w in dictionary:
            self.d[self.abbv(w)].add(w)

    def abbv(self, word: str) -> str:

        return f"{word[0]}{len(word) - 2}{word[-1]}" if len(word) > 2 else word

    def isUnique(self, word: str) -> bool:

        abbv = self.abbv(word)

        if abbv in self.d:
            if len(self.d[abbv]) == 1 and word in self.d[abbv]:
                return True
            else:
                return False
        else:
            return True

