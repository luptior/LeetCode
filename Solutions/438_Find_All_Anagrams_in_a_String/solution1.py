from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []

        result = []

        d1 = Counter(p)

        n = len(p)
        i = 0

        d2 = Counter(s[:n])

        d3 = defaultdict(int)

        for k, v in d1.items():
            d3[k] += v

        for k, v in d2.items():
            d3[k] -= v

        if all(v == 0 for k, v in d3.items()):
            result.append(0)

        while i + n < len(s):

            d3[s[i]] += 1
            d3[s[i + n]] -= 1

            if all(v == 0 for k, v in d3.items()):
                result.append(i + 1)

            i += 1

        return result