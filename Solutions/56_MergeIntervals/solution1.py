# TODO

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:

        s = set([])
        for interval in intervals:
            r = set(range(interval[0], interval[1]+1))
            s = s | r

        s = list(s)
        s.sort()

        result = []
        curr = []

        for i, d in enumerate(s):
            if not curr:
                curr.append(d)
            else:
                if i < len(s)-1 and s[i+1] == d+1:
                    continue
                else:
                    curr.append(d)
                    result.append(curr)
                    curr = []

        return result



if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    s = Solution()
    print(s.merge(intervals))