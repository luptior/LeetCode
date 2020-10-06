from collections import deque

import math
class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:

        if k == 1: return nums

        q = deque()

        def clean(i: int):

            # ii is the index

            if q and q[0] == i - k:  # remove the last head
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                # sorted so remove from end
                q.pop()

        max_idx = 0

        for i in range(k):

            clean(i)
            q.append(i)

            if nums[i] > nums[max_idx]:
                max_idx = i

        result = [nums[max_idx]]

        for i in range(k, len(nums)):
            clean(i)
            q.append(i)

            result.append(nums[q[0]])

        return result





