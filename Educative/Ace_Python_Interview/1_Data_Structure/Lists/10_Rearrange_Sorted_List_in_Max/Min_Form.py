"""
Problem Statement#
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index
will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and
so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and
the odd-numbered indices will have the smallest numbers in ascending order.

Input:#
A sorted list

Output:#
A list with elements stored in max/min form

Sample Input#
lst = [1,2,3,4,5]
Sample Output#
lst = [5,1,4,2,3]
"""


def max_min(lst: []) -> []:
    result = [0] * len(lst)

    for i, v in enumerate(lst):
        ind = 2 * i + 1 if 2 * i + 1 <= len(lst) - 1 else len(lst) - 2 * i -2
        print(i, ind)
        result[ind] = v

    return result


def max_min2(lst):
    # Return empty list for empty list
    if not lst:
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    print(max_min([1, 2, 3, 4, 5]))

    """
    Input	Expected Output	Actual Output	Reason
    max_min([1, 2, 3, 4, 5, 6, 7])	[7, 1, 6, 2, 5, 3, 4]	[7, 1, 6, 2, 5, 3, 4]	Succeeded
    max_min([1, 2, 3, 4, 5])	[5, 1, 4, 2, 3]	[5, 1, 4, 2, 3]	Succeeded
    max_min([])	[]	[]	Succeeded
    max_min([1, 1, 1, 1, 1])	[1, 1, 1, 1, 1]	[1, 1, 1, 1, 1]	Succeeded
    max_min([-10, -1, 1, 1, 1, 1])	[1, -10, 1, -1, 1, 1]	[1, -10, 1, -1, 1, 1]	Succeeded
    """


"""




"""