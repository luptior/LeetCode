"""
Runtime: 128 ms, faster than 98.10% of Python3 online submissions for Coin Change 2.
Memory Usage: 14.4 MB, less than 67.52% of Python3 online submissions for Coin Change 2.
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]