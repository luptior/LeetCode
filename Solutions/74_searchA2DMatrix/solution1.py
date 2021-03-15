def searchMatrix( matrix: [[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False

    if len(matrix[0]) == 0:
        return False

    target_line = 0

    for i in range(len(matrix)):

        if matrix[i][0] > target:  # first element is larger than target
            if i != 0:
                target_line = i - 1
                # print("break1")
                break
            else:
                print("false1")
                return False
        elif matrix[i][0] == target:  # first element is the target
            return True
        elif i == len(matrix) - 1:  # the last line situation
            if matrix[i][-1] > target:  # biggest element in the matrix
                target_line = i
                # print("break2")
                break
            elif matrix[i][-1] == target:
                return True
            else:
                print("false2")
                return False

    # binary seearch

    if target in matrix[target_line]:
        return True
    else:
        print("false3")
        return False


if __name__ == '__main__':
    A = [[1, 3]]
    t = 3

    print(searchMatrix(A, t))