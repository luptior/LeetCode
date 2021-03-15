from collections import deque
import math



def insert(l : list, e: int):
    len_l = len(l)

    for i in range( len_l - 1, -1, -1):
        if l[i] <= e:
            l = l[:i+1] + [e] + l[i+1:]
            break
    if len_l == len(l):
        l.append(e)

    return l


def kthSmallest(matrix:[[int]], k: int) -> int:

    n = len(matrix)
    visited = []
    rank = []
    wl = deque([[0, 0]])

    while wl:

        # print(wl, rank)
        i, j = wl.popleft()
        if (i, j) not in visited:
            visited.append((i,j))
        else:
            continue

        val = matrix[i][j]

        len_rank = len(rank)
        if len(rank) < k:
            rank = insert(rank, val)

        else:
            if val >= rank[-1]: # no need to check the following
                continue
            else:
                rank.remove(rank[-1])
                rank = insert(rank, val)

        if i+1 < n and j < n and (i+1, j) not in visited:
            # print((i+1, j),  visited)
            wl.append([i+1, j])
        if j+1 < n and i < n and (i, j+1) not in visited:
            # print((i, j+1), visited)
            wl.append([i, j+1])

    return max(rank)


if __name__ == '__main__':
    matrix = [[1, 3, 5], [6, 7, 12], [11, 14, 14]]
    k = 6

    print(kthSmallest(matrix, k))

    l = [1 ]
    e = 6

    # print(insert(l, e))