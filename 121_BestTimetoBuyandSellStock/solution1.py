from collections import deque

class Solution:
    def maxProfit(self, prices: [int]) -> int:

        if len(prices) == 0: return 0

        left = [prices[0]]

        right = deque([prices[-1]])

        for i in range(1, len(prices)):
            left.append(min(prices[i], left[i-1]))

        for i in range(len(prices)-1, 0, -1):
            right.appendleft(max(prices[i], right[0]))

        diff = [ right[i]-left[i] for i in range(len(prices))]

        return max(diff)


if __name__ == '__main__':
    example = [7,1,5,3,6,4]

    s = Solution()

    print(s.maxProfit(example))