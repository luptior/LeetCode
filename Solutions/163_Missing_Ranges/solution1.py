"""
TLE
"""

class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:

        start = None
        end = None

        result = []

        for i in range(lower, upper + 1):

            if i not in nums:

                if start is None:
                    start = i
                else:
                    if end is None:
                        if i > start + 1:
                            result.append(f"{start}")
                            start, end = i, None
                        else:
                            end = i

                    elif i == end + 1:
                        end = i
                    else:
                        result.append(f"{start}->{end}")
                        start, end = i, None

        if start is not None and end is not None:
            result.append(f"{start}->{end}")
        elif start is not None:
            result.append(f"{start}")

        return result