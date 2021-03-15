"""
Runtime: 1008 ms, faster than 27.40% of Python3 online submissions for Sliding Window Median.
Memory Usage: 16 MB, less than 66.45% of Python3 online submissions for Sliding Window Median.

"""

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def removeNum(self, num):

        if self.minheap and num >= self.minheap[0]:
            self.minheap.remove(num)
            heapq.heapify(self.minheap)
        else:
            self.maxheap.remove(-num)
            heapq.heapify(self.maxheap)

    def addNum(self, num) -> None:

        # insert
        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # re-balance
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        elif len(self.minheap) + 1 < len(self.maxheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:

        if len(self.minheap) == len(self.maxheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]


class Solution:

    def medianSlidingWindow(self, nums: [int], k: int) -> [float]:

        if k == 0: return

        window = MedianFinder()
        median = []

        for i in range(k):
            window.addNum(nums[i])

        median.append(window.findMedian())

        for i in range(1, len(nums) - k + 1):
            window.removeNum(nums[i - 1])
            window.addNum(nums[i + k - 1])
            median.append(window.findMedian())

        return median


if __name__ == '__main__':
    s = Solution()

    nums = [1,2]
    k = 1

    print(s.medianSlidingWindow(nums, k))
