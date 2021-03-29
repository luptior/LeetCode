# Definition for singly-linked list.
"""
Runtime: 48 ms, faster than 80.96% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.7 MB, less than 11.04% of Python3 online submissions for Linked List Cycle II.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        visited = set()

        curr = head

        while curr and curr not in visited:
            visited.add(curr)
            curr = curr.next

        if not visited:
            return None

        return curr