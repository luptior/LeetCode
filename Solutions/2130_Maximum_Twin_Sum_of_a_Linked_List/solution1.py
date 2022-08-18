from typing import Optional
from Solutions import ListNode
from collections import deque

"""
Runtime: 1431 ms, faster than 49.15% of Python3 online submissions for Maximum Twin Sum of a Linked List.
Memory Usage: 55.5 MB, less than 16.26% of Python3 online submissions for Maximum Twin Sum of a Linked List.
"""

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        d = deque()

        while head:
            d.append(head.val)
            head = head.next

        maxi = 0
        while d:
            maxi = max(maxi, d.popleft() + d.pop())

        return maxi