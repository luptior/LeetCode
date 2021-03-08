"""
Runtime: 40 ms, faster than 56.73% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 14.2 MB, less than 86.08% of Python3 online submissions for Remove Outermost Parentheses.
"""

class Solution:

    def removeOuterParentheses(self, S: str) -> str:

        count = 0
        stack = 0
        result = ""

        for s in S:

            if s == "(" and count == 0:
                count += 1
            elif s == ")" and count == 1 and stack == 0:
                count -= 1
            else:
                if s == "(":
                    stack += 1
                else:
                    stack -= 1
                result += s

            # print(s, count, result)

        return result