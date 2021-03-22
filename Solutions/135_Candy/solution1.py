from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        candy1 = [1] * len(ratings)
        candy2 = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy1[i] = candy1[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy2[i] = candy2[i + 1] + 1

        return sum([max(candy1[i], candy2[i]) for i in range(len(ratings))])