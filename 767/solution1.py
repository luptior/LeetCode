from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:

        result = ["*"] * len(S)

        d = Counter(S)

        if d.most_common(1)[0][1] > len(S) // 2 + len(S) % 2:
            return ""

        else:

            k = d.most_common(1)[0][0]
            for i in range(0, len(S), 2):
                if d[k] > 0:
                    result[i] = k
                    d[k] -= 1
                else:
                    del d[k]
                    k = d.most_common(1)[0][0]
                    result[i] = k
                    d[k] -= 1

            for i in range(1, len(S), 2):
                if d[k] > 0:
                    result[i] = k
                    d[k] -= 1
                else:
                    del d[k]
                    k = d.most_common(1)[0][0]
                    result[i] = k
                    d[k] -= 1

        return "".join(result)
