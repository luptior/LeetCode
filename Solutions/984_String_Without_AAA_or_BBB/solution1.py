"""
Runtime: 20 ms, faster than 98.55% of Python3 online submissions for String Without AAA or BBB.
Memory Usage: 14.2 MB, less than 81.82% of Python3 online submissions for String Without AAA or BBB.

"""


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        # if 2a+2 > b or 2b+2 > a:

        result = ""

        while a > 0 or b > 0:

            if a == 0 and b == 0:
                break

            elif a == 0 or b == 0:

                result += "a" * a + "b" * b
                break

            if a > b and a >= 2:
                if not result or result[-1] != "a":
                    result += "aab"
                else:
                    result += "baa"
                a -= 2
                b -= 1
            elif a < b and b >= 2:
                if not result or result[-1] != "b":
                    result += "bba"
                else:
                    result += "abb"
                b -= 2
                a -= 1

            else:
                if not result or result[-1] != "a":
                    result += "ab"
                else:
                    result += "ba"
                a -= 1
                b -= 1

        return result




