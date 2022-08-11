# Definition for singly-linked list.
from typing import Optional

"""
Runtime: 65 ms, faster than 36.31% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 32.66% of Python3 online submissions for Merge Two Sorted Lists.

This is a recursive solution
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list1.val <= list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
            return head
        else:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)
            return head


if __name__ == '__main__':
    s = Solution()