# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseLinkedList(self, head, k):

        new_head, ptr = None, head
        while k:

            next_node = ptr.next

            ptr.next = new_head
            new_head = ptr

            ptr = next_node

            k -= 1

        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ptr = head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reversedHead = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead

        return head


def printlist(head: ListNode ):

    s = []
    while head:
        s.append(head.val)
        head = head.next

    print(s)



if __name__ == '__main__':
    s = Solution()

    l = [1,2,3,4,5]

    last = None

    for i in range(len(l)-1, -1, -1):
        last = ListNode(l[i], last)

    printlist(last)
    s.reverseKGroup(last, 2)
    # print(s.reverseKGroup(last, 2))
