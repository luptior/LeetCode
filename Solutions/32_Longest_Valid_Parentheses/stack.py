"""
Runtime: 44 ms, faster than 71.71% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14.7 MB, less than 54.21% of Python3 online submissions for Longest Valid Parentheses.

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]

        curr = 0
        maxi = 0

        for i, c in enumerate(s):

            if c == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    curr = i - stack[-1]
                    maxi = max(curr, maxi)

        return maxi