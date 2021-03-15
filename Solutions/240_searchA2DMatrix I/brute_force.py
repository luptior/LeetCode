def searchMatrix(matrix: [[int]], target: int) -> bool:
    for l in matrix:

        if target < l[0] or target > l[-1]:
            continue

        if target in l:
            return True

    return False