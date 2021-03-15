# brute force
# Runtime: 1012 ms, faster than 5.17% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.3 MB, less than 15.64% of Python3 online submissions for Merge Intervals.

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:

        result = intervals[:]

        for interval in intervals:

            partial_merged = {}
            for i, r in enumerate(result):
                tmp = self.overlap(interval, r)
                if tmp:
                    partial_merged[i] = tmp

            print(partial_merged)

            if len(partial_merged) > 0:
                min_k = min(partial_merged.keys())
                values = list(partial_merged.values())
                while len(values) > 1:
                    val = values.pop()
                    values[0] = self.overlap(values[0], val)
                result[min_k] = values[0]

                keys = list(partial_merged.keys())
                keys.remove(min_k)

                new_results = [ v for k,v in enumerate(result) if k not in keys]

                result = new_results

        return result

    def overlap(self, interval1, interval2):
        x1, y1 = interval1
        x2, y2 = interval2

        r1 = set(range(x1, y1+1))
        r2 = set(range(x2, y2+1))

        if len(r1 & r2) == 0:
            return []
        else:
            r1 = r1 | r2
            return [min(r1), max(r1)]


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    s = Solution()
    print(s.merge(intervals))