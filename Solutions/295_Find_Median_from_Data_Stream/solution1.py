import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:

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
            return (-self.maxheap[0] + self.minheap[0] )/2
        else:
            return -self.maxheap[0]


if __name__ == '__main__':

    s = MedianFinder()

    s.addNum(1)
    s.addNum(2)
    assert s.findMedian() == 1.5
    s.addNum(3)
    print(s.maxheap, s.minheap)
    assert s.findMedian() ==  2