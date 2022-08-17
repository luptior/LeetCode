"""
Maximum sublist sum: An overview#
Given an unsorted list A, the maximum sum sub list is the sub list (contiguous elements) from
A for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum sub list.
This problem is a tricky one because the list might have negative integers in any position, so we have to cater to those
 negative integers while choosing the continuous sublist with the largest positive values.

 Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.

Partial function definition#
def find_max_sum_sublist(lst):
  pass
Input#
a list lst
Output#
a number (maximum subarray sum)

sample in put
[-4, 2, -5, 1, 2, 3, 6, -5, 1]

Sample output#
largest_sum = 12

"""
import sys
from collections import deque

def find_max_sum_sublist(lst):
    # not wokring now
    left_right = []
    for i, x in enumerate(lst):
        left_right.append( x+left_right[-1] if i > 0 else x)

    right_left = deque()
    for i in reversed(range(len(lst))):
        right_left.appendleft( lst[i] + right_left[0] if i < len(lst) - 1 else lst[i])

    print(left_right)
    print(right_left)

    maxi = -sys.maxsize

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            maxi = max(left_right[i] - right_left[j], maxi)

    return maxi

if __name__ == '__main__':
    s = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    s2 = [12, 10, 7, -5, 15, 6]
    print(find_max_sum_sublist(s))
