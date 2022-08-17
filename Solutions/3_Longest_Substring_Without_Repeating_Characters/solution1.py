from collections import defaultdict

"""
Runtime: 141 ms, faster than 29.34% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 13.97% of Python3 online submissions for Longest Substring Without Repeating 
Characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        d = defaultdict(int)
        maxi = 0

        i = j = 0
        d[s[i]] += 1

        while j + 1 < len(s):

            j += 1

            while s[j] in d and i < j:
                del d[s[i]]
                i += 1

            d[s[j]] += 1
            maxi = max(len(d), maxi)

        return maxi


if __name__ == '__main__':
    s = Solution()

    print(s.lengthOfLongestSubstring("abcabcbb"))