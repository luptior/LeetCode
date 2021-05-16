class Solution:
    def maxPower(self, s: str) -> int:

        candidates = []

        prev = ""

        for c in s:

            if c != prev:
                candidates.append(1)
                prev = c
            else:
                candidates[-1] += 1

        return max(candidates) if candidates else 0