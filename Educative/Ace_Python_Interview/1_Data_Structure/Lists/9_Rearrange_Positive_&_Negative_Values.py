"""
Problem Statement#
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.
Output#
A list with negative elements at the left and positive elements at the right

Sample Input#
[10,-1,20,4,5,-9,-6]
Sample Output#
[-1,-9,-6,10,20,4,5]
"""

from collections import deque


"""
O(n)
"""
def rearrange(lst):

    d = deque()

    for e in lst:
        if e >= 0:
            d.append(e)
        else:
            d.appendleft(e)

    return [e for e in d]


if __name__ == '__main__':
    print(rearrange([10, -1, 20, 4, 5, -9, -6]))