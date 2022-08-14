"""
Problem Statement#
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).

Input#
Two sorted lists.

Output#
A merged and sorted list consisting of all elements of both input lists.

Sample Input#
list1 = [1,3,4,5]
list2 = [2,6,7,8]
Sample Output#
arr = [1,2,3,4,5,6,7,8]
"""

from collections import deque


""" new list """
def merge_lists1(lst1, lst2):
    result = []

    d1 = deque(lst1)
    d2 = deque(lst2)

    while len(d1) != 0 and len(d2) != 0 :
        if d1[0] <= d2[0]:
            result.append(d1.popleft())
        else:
            result.append(d2.popleft())

    if len(d1) != 0:
        result += list(d1)

    if len(d2) != 0:
        result += list(d2)

    return result

""" merge in place """
def merge_lists2(lst1, lst2):

    ind1 = 0
    ind2 = 0

    while ind1 < len(lst1) and ind2 < len(lst2):

        if list1[ind1] >= list2[ind2]:
            list1.insert(ind1, list2[ind2])
            ind2 += 1
        ind1 += 1

    if ind2 < len(lst2):
        lst1 += list2[ind2:]


if __name__ == '__main__':
    list1 = [4]
    list2 = [1,2,3,5,6]

    merge_lists2(list1, list2)

    print(list1)