class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0

        return haystack.index(needle) if needle in haystack else -1