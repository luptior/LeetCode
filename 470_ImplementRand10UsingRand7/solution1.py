
from random import randint
from collections import Counter

def rand7():
    return randint(1, 7)


def rand10():
    """
    :rtype: int
    """

    index = 41

    while index > 40:
        row = rand7()
        col = rand7()

        index = col + (row - 1) * 7

    return 1 + (index - 1) % 10;

if __name__ == '__main__':

    result = Counter([rand10() for i in range(10000)])

    print(result)
