class Solution:
    def minWindow(self, S, T):
        # Find - Get ending point of subsequence starting after S[s]
        def find_subseq(s):
            t = 0
            while s < len(S):
                if S[s] == T[t]:
                    t += 1
                    if t == len(T):
                        break
                s += 1

            return s if t == len(T) else None  # Ensure last character of T was found before loop ended

        # Improve - Get best starting point of subsequence ending at S[s]
        def improve_subseq(s):
            t = len(T) - 1
            while t >= 0:
                if S[s] == T[t]:
                    t -= 1
                s -= 1

            return s + 1


        s, min_len, min_window = 0, float('inf'), ''

        while s < len(S):
            end = find_subseq(s)  # Find end-point of subsequence
            if not end:
                break

            start = improve_subseq(end)  # Improve start-point of subsequence

            if end - start + 1 < min_len:  # Track min length
                min_len = end - start + 1
                min_window = S[start:end + 1]

            s = start + 1  # Start next subsequence search

        return min_window

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("abcdebdde", "bde"))