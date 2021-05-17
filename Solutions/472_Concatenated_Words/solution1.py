from functools import lru_cache
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = set([word for word in words if word])  # Filter Empty Words
        #
        # Find Compatible substring lengths using binary search
        nlens = sorted(set(map(len, words)))

        def getsizes(L, i):
            # BISECT USAGE:
            #     bisect_left   ->  a[lo:i] <  x <= a[i:hi]
            #     bisect_right  ->  a[lo:i] <= x <  a[i:hi]
            if i:
                Lj = bisect_right(nlens, L)  # include L
            else:
                Lj = bisect_left(nlens, L)  # exclude L
            # Yield Reversed without delay
            for j in range(Lj - 1, -1, -1):
                yield nlens[j]

        #
        # DFS matching function:
        @lru_cache(None)
        def dfs(i, word, L):

            # print(i, word, L)
            if i == L:
                return True
            #

            for a in getsizes(L - i, i):
                substr = word[i:i + a]
                if substr in words and dfs(i + a, word, L):
                    return True
            return False

        #
        # Final Loop:
        res = []
        for word in words:
            if dfs(0, word, len(word)):
                res.append(word)
        #
        return res