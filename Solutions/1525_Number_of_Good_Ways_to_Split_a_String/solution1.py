import collections


class Solution:
    def numSplits(self, s: str) -> int:

        if len(s) <= 1:
            return 0

        if len(s) == 2:
            return 1 if s[0] == s[1] else 0

        left = collections.Counter(s[0])
        right = collections.Counter(s[1:])

        result = 0

        for i in range(1, len(s)):

            # print(left,  right)

            if len(left) == len(right):
                # print(left,  right)
                result += 1

            left += collections.Counter(s[i])
            right -= collections.Counter(s[i])

        return result


