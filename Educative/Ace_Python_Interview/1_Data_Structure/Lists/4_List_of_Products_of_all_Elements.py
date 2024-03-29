"""
Problem Statement#
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:#
A list of numbers (could be floating points or integers)

Output:#
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input#
arr = [1,2,3,4]
Sample Output#
arr = [24,12,8,6]
"""
from math import prod

"""
O(n) solution
"""


def find_product(lst):
    left_prod = 1
    right_prod = prod(lst[1:])

    result = [right_prod]

    for i in range(1, len(lst)):
        left_prod *= lst[i - 1]
        right_prod = right_prod // lst[i] if right_prod != 0 else 0
        print(left_prod, right_prod)
        result.append(right_prod * left_prod)

    return result

"""
better o(n) without the division which is slower
"""

def find_product2(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele

    print(product)
    # get product starting from right
    right = 1
    for i in reversed(range(len(lst))):
        product[i] = product[i] * right
        right = right * lst[i]
        print(product)

    return product


if __name__ == '__main__':
    arr = [1, 2, 3, 4]

    print(find_product2(arr))
