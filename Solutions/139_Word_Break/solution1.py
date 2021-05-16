"""
Time Limit Exceeded
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)

        def step(start):

            if start == len(s): return True

            for end in range(start + 1, len(s) + 1):

                # print(start, end, s[start: end] )

                if s[start: end] in wordDict and step(end):
                    return True
            return False

        return step(0)
