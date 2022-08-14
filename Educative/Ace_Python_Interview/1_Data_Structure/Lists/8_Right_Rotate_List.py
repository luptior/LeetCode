"""

Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements
 will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

Input#
A list and a positive number by which to rotate that list

Output:#
The given list rotated by k elements

"""


def right_rotate(lst, k):

    if k == 0 or not lst: return lst

    k = k%len(lst)

    return lst[len(lst)-k:] + lst[:len(lst)-k]


if __name__ == '__main__':
    lst = [300, -1, 3, 0]
    k = 3

    print(right_rotate(lst, k))