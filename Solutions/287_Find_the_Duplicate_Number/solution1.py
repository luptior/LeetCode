"""
Runtime: 64 ms, faster than 75.73% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 18.5 MB, less than 11.84% of Python3 online submissions for Find the Duplicate Number.


Set implementation but space complexity is larger than expected.

"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        visited = set()

        for n in nums:
            if n in visited:
                return n
            else:
                visited.add(n)