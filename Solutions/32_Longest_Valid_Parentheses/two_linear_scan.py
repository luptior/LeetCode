"""
Runtime: 44 ms, faster than 71.71% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14.3 MB, less than 96.02% of Python3 online submissions for Longest Valid Parentheses.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        curr, left, right, maxi = 0, 0, 0, 0

        for c in s:

            if c == "(":
                left += 1
            else:
                right += 1

            if right == left:
                curr = left + right
                maxi = max(maxi, curr)

            if right > left:
                left, right = 0, 0

        curr, left, right = 0, 0, 0

        for c in s[::-1]:

            if c == "(":
                left += 1
            else:
                right += 1

            if right == left:
                curr = left + right
                maxi = max(maxi, curr)

            if left > right:
                left, right = 0, 0

        return maxi