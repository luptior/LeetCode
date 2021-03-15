# sliding windows

from collections import defaultdict


def totalFruit(tree: [int]) -> int:

    if len(tree) <= 2:
        return len(tree)

    d = defaultdict(int)
    i = j = 0

    while j < len(tree):
        d[tree[j]] += 1
        while len(tree) > 2:
            d[tree[i]] -= 1
            if d[tree[i]] == 0:
                del d[tree[i]]
            i += 1
        j += 1

        print(d)








if __name__ == '__main__':
    print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))