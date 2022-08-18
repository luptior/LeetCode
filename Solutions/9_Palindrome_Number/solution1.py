"""
Runtime: 83 ms, faster than 72.22% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 59.89% of Python3 online submissions for Palindrome Number.
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0: return False

        if 0 <= x < 10: return True

        l = []

        mid, is_even = (len(str(x)) // 2, False) if len(str(x)) % 2 == 1 else (len(str(x)) // 2 -1, True)

        for i, c in enumerate(str(x)):
            if i < mid:
                l.append(c)
            elif i == mid:
                if is_even:
                    l.append(c)
            else:
                if l.pop() != c:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10101))