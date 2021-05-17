from functools import lru_cache
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = [word for word in words if word]

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