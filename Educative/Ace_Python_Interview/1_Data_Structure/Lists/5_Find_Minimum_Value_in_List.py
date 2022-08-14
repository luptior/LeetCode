"""
Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input:#
A list of integers

Output:#
The smallest number in the list

Sample Input#
arr = [9,2,3,6]
Sample Output#
2

"""

from sys import maxsize


"""
iterate through the list which is O(n)
"""
def findMinimum(lst):

    mini = maxsize

    for v in lst:
        mini = min(mini, v)

    return mini


if __name__ == '__main__':

    print(findMinimum([9,2,3,6]))