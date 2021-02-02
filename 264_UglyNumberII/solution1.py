from collections import deque

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        l = set([1, 2, 3, 4, 5, 6])

        if n <= 6:
            return n
        else:
            curr = 7
            while len(l) < n:
                tmp = curr
                if tmp % 2 == 0:
                    tmp = tmp // 2
                if tmp % 3 == 0:
                    tmp = tmp // 3
                if tmp % 5 == 0:
                    tmp = tmp // 5

                if tmp in l:
                    l.add(curr)
                curr += 1

                # print(curr, tmp, l)
            return curr - 1


if __name__ == '__main__':
    n = 447
    s = Solution()

    print(s.nthUglyNumber(n))
