"""
Just as heads and tails are polar opposites, this function is the opposite of what we saw in the last lesson. However,
it is just as simple.

We need to insert a new object at the end of the linked list. You can naturally guess, that this newly added node will
 point to None as it is at the tail.

Input#
A linked list and an integer value.

Output#
The updated linked list with the value inserted.

Sample Input#
Linked List = 0->1->2
integer = 3
Sample Output#
Linked List = 0->1->2->3

"""


from LinkedinList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list


def insert_at_tail(lst:LinkedList, value):
    # Write - Your - Code

    node = Node(value)
    if lst.is_empty():
        return LinkedList(node)
    else:
        curr = lst.get_head()
        while curr.next_element:
            curr = curr.next_element
        curr.next_element = node

    pass
