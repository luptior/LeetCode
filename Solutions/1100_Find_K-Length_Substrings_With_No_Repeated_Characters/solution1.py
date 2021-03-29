from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:

        if len(S) < K:
            return 0

        result = 0
        d = Counter(S[:K])  # counts 1
        d2 = {}  # counts > 1

        for k, v in d.items():
            if v > 1:
                d2[k] = v

        for k in d2.keys():
            del d[k]

        # # print(d2)

        if len(d2) == 0:
            result += 1

            # print(result)

        for i in range(1, len(S) - K + 1):

            pre = S[i - 1]
            new = S[i + K - 1]

            if pre in d2:
                if d2[pre] == 2:
                    del d2[pre]
                    d[pre] = 1
                elif d2[pre] > 2:
                    d2[pre] -= 1
            else:
                del d[pre]

            if new in d:
                del d[new]
                d2[new] = 2
            elif new in d2:
                d2[new] += 1
            else:
                d[new] = 1

                if len(d2) == 0:
                    # print(i, pre, new, d, d2, result)
                    result += 1

        return result









