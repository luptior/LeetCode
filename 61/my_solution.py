# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or head.next is None:
            return head

        if k == 0:
            return head

        length = 1
        ptr = head

        d = {0: head}

        while ptr.next:
            ptr = ptr.next
            length += 1
            d[length - 1] = ptr

        k = k % length

        if k == 0:
            return head

        d[length - k - 1].next = None

        head = d[length - k]

        d[length - 1].next = d[0]

        return head


