"""
Given a list, find the first integer which is unique in the list. Unique means the number does not repeat and appears only once in the whole list. Implement your solution in Python and see if it runs correctly!

We'll cover the following

Problem Statement
Input
Output
Sample Input
Sample Output
Coding Challenge
Problem Statement#
Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

Input#
A list of integers

Output#
The first unique element in the list

Sample Input#
[9,2,3,2,6,6]
Sample Output#
9
"""
from collections import defaultdict

"""
O(n) for both
"""
def find_first_unique(lst):

    # space complexity O(2*n)
    count = defaultdict(int)
    order = []

    # O(n)
    for v in lst:
        if v not in count:
            order.append(v)
        count[v] += 1

    # O(n)
    for ele in order:
        if count[ele] == 1:
            return ele

    # assume there garantteed to be  result


if __name__ == '__main__':
    print(find_first_unique([9,2,3,2,6,6]))

