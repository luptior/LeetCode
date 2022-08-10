"""
pretty bad
Runtime: 340 ms, faster than 5.01% of Python3 online submissions for Is Subsequence.
Memory Usage: 78 MB, less than 5.62% of Python3 online submissions for Is Subsequence.
"""
from functools import lru_cache


class Solution:

    @lru_cache
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False
        elif len(s) == len(t):
            return s == t
        elif len(s) == 0:
            return True
        else:
            if s[0] == t[0]:
                return self.isSubsequence(s[1:], t[1:]) or self.isSubsequence(s, t[1:])
            else:
                return self.isSubsequence(s, t[1:])