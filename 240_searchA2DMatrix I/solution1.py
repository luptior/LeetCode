from collections import deque


def searchMatrix(matrix: [[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    visited = []
    wl = deque([[0, 0]])

    def bfs(wl):

        curr = wl.popleft()

        if curr not in visited:
            visited.append(curr)
        else:
            return False

        i, j = curr

        print(matrix[i][j])

        if matrix[i][j] > target:
            return False
        elif matrix[i][j] < target:
            while i + 1 < m:
                i += 1
                if matrix[i][j] < target:
                    continue
                else:
                    if [i-1, j] not in visited:
                        wl.append([i-1, j])
                    break
            while j + 1 < n:
                j += 1
                if matrix[i][j] < target:
                    continue
                else:
                    if [i, j-1] not in visited:
                        wl.append([i, j-1])
                    break
            return False
        else:
            return True

    # print(wl)
    while wl:
        if bfs(wl):
            return True
        print(wl)

    return False


if __name__ == '__main__':
    a = [[1, 4, 7, 11, 15], \
         [2, 5, 8, 12, 19], \
         [3, 6, 9, 16, 22], \
         [10, 13, 14, 17, 24],\
         [18, 21, 23, 26, 30]]
    t = 5

    print(searchMatrix(a, t))
