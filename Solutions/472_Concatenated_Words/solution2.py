"""
Runtime: 420 ms, faster than 86.37% of Python3 online submissions for Concatenated Words.
Memory Usage: 19.9 MB, less than 61.92% of Python3 online submissions for Concatenated Words.
"""

from functools import lru_cache
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = set([word for word in words if word])

        nlens = sorted(set(map(len, words)))

        # print(nlens)

        @lru_cache()
        def dfs(i, word, L):

            if i == L:
                return True

            for sub in nlens[::-1]:

                if sub < L and sub <= L - i:

                    substr = word[i:i + sub]

                    if substr in words and dfs(i + sub, word, L):
                        return True

            return False

        res = []
        for word in words:
            if dfs(0, word, len(word)):
                res.append(word)

        return res