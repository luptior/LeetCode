"""
Introduction#
Here is a short guide to these challenge lessons.

The function definition is always given in the problem statement with the expected arguments and function name to be
used as is in the solution. If you change it, your code will not compile
The skeleton code given has a function definition which only has the pass keyword in the body. It does exactly what it
sounds like it does: nothing. It’s just there as a placeholder. Delete it and add your code in.
When you do get compile-time errors, they will sometimes refer to line numbers and code which you did not write. That is
 fine; that is just our evaluation code. When in doubt, refer to the solution given and paste that in.
Sometimes you will have to return from functions in a form that aligns with the test cases. Your solution may not be
incorrect, but the return value might not be what the evaluation code expects. For example, you might return two numbers
 in a list, but our test cases might expect a tuple. Watch out for that. Good luck! 🍀
"""


def remove_even(l: []) -> []:
    return [x for x in l if x % 2 != 0]


if __name__ == '__main__':
    my_list = [1, 2, 4, 5, 10, 6, 3]
    print(remove_even(my_list))