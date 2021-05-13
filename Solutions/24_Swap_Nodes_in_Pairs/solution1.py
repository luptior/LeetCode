# Definition for singly-linked list.

"""
Runtime: 28 ms, faster than 83.11% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.3 MB, less than 15.28% of Python3 online submissions for Swap Nodes in Pairs.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        tmp = ListNode()

        prev = tmp
        curr = head
        nxt = head.next

        while nxt is not None:

            prev.next = nxt
            curr.next = nxt.next
            nxt.next = curr

            prev = curr
            curr = curr.next
            if curr:
                nxt = curr.next
            else:
                break

        return tmp.next
