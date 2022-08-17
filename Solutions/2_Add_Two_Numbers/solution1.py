# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Runtime: 110 ms, faster than 47.67% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.8 MB, less than 99.35% of Python3 online submissions for Add Two Numbers.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = head = ListNode()

        prev = 0

        while l1 or l2:

            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            s = prev + dig1 + dig2
            dig = s % 10
            prev = s // 10
            curr.next = ListNode(val=dig)
            curr = curr.next

        return head.next



