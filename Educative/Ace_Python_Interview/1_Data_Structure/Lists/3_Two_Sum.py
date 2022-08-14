"""
Problem Statement#
In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

Input#
A list and a number k

Output#
A list with two integers a and b that add up to k

Sample Input#
lst = [1,21,3,14,5,60,7,6]
k = 81
Sample Output#
lst = [21,60]

"""


"""
basically brute force, n^2
"""
def find_sum1(lst, k):

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == k:
                return [lst[i], lst[j]]


"""
sorting
"""
def find_sum2(lst, k):

    lst = sorted(lst)

    head = 0
    tail = len(lst) - 1

    while lst[head] + lst[tail] != k:
        if lst[head] + lst[tail] < k:
            head += 1
        else:
            tail -= 1

    return [lst[head], lst[tail]]

if __name__ == '__main__':
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81

    print(find_sum2(lst, k))