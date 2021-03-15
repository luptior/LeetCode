class Solution:
    def minEatingSpeed(self, piles: [int], H: int) -> int:

        """
        :param piles:
        :param H:  minimum hours
        :return: speed K
        """
        K = min(piles)

        count = lambda x: x // K if x % K == 0 else x // K + 1

        counts = sum([count(p) for p in piles])

        print(counts)

        left = 1
        right = max(piles)


        while left < right:


        return K


if __name__ == '__main__':
    piles = [312884470]
    H = 312884469

    s = Solution()
    print(s.minEatingSpeed(piles, H))
