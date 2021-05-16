from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        counts = [amount + 1] * (amount + 1)
        counts[0] = 0

        # value correspondes to the counts of coins needed for that position

        for i in range(1, amount + 1):

            for c in coins:
                if i - c >= 0:
                    counts[i] = min(counts[i], counts[i - c] + 1)

        return counts[amount] if counts[amount] < amount + 1 else -1


