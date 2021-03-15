# simple stack counts:
# 46% speed

class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        if len(S) == 0: return 0

        stack = 0
        count = 0

        for x in S:
            if x == "(":
                stack += 1
            else:
                if stack > 0:
                    stack -= 1
                else:
                    count += 1

        return stack + count


if __name__ == '__main__':
    # Input: "()))(("
    # Output: 4

    s = Solution()
    i = "()))(("

    print(s.minAddToMakeValid(i))