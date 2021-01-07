class Solution:
    def maxProfit(self, prices: [int]) -> int:

        if len(prices) <= 1:
            return 0

        own = None
        profit = 0

        for i in range(len(prices)-1):
            if own is None and prices[i] < prices[i+1]:
                own = prices[i]
            elif own is not None and prices[i] < prices[i+1]:
                continue
            elif own is not None and prices[i] > prices[i+1]:
                profit += prices[i] - own
                own = None

            print(prices[i], own, profit)

        if own is not None and prices[-1] > own:
            profit += prices[-1] - own

        return profit


if __name__ == '__main__':
    example = [3,3,5,0,0,3,1,4]

    s = Solution()

    print(s.maxProfit(example))