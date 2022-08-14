"""

Given a list of size n, can you find the second maximum element in the list? Implement your solution in Python and see
if your output matches the correct output!

Implement a function find_second_maximum(lst) which returns the second largest element in the list.

Input:#
A List

Output:#
Second largest element in the list

Sample Input#
[9,2,3,6]
Sample Output#
6
"""
from sys import maxsize


"""
one traverse linear, best solution
"""
def find_second_maximum(lst):

    first, second = -maxsize, -maxsize

    for e in lst:
        if e > first:
            first, second = e, first
        elif second < e < first:
            second = e

    return second


if __name__ == '__main__':
    print(find_second_maximum([9,2,3,6]))