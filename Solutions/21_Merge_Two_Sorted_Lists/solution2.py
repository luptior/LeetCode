# Definition for singly-linked list.
from typing import Optional

"""
Runtime: 57 ms, faster than 54.91% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 32.66% of Python3 online submissions for Merge Two Sorted Lists.

This is a iterative solution
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = head = ListNode()

        while list1 is not None or list2 is not None:

            if list2 is None or (list1 is not None and list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
            elif list1 is None or (list2 is not None and list1.val > list2.val):
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        return head.next


if __name__ == '__main__':
    s = Solution()