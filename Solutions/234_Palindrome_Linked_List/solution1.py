from typing import Optional
from collections import deque

"""
Runtime: 1190 ms, faster than 53.64% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.5 MB, less than 7.68% of Python3 online submissions for Palindrome Linked List.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        d = deque()

        while head:
            d.append(head.val)
            head = head.next

        while d:
            if len(d) == 1:
                return True

            if d.popleft() != d.pop():
                return False

        return True
