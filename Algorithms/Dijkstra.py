from collections import Counter


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        d = Counter(s)  # O(n)

        # the char that has total number > k, pruning some search
        candidate = set([])

        for c, v in d.items():
            if v >= k:
                candidate.add(c)

        # print(candidate)

        result = list(s)

        i = 0

        while i < len(result) - k + 1:

            # print(i, result[i], )

            if result[i] in candidate and all(
                    c == result[i] for c in result[i:i + k]):  # the condition is met, eliminate

                for _ in range(k):
                    result.pop(i)

                i = 0
            else:
                i += 1

        return "".join(result)



if __name__ == '__main__':

