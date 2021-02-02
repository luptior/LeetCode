from collections import Counter


def fillSudoku(board: [[str]]):



def isValidSudoku(board: [[str]]) -> bool:
    for row in board:
        if not legit_list(row):
            return False

    for i in range(9):
        if not legit_list([row[i] for row in board]):
            return False

    for i in range(3):
        for j in range(3):
            x, y = i * 3, j * 3
            l = []
            for row in range(x, x + 3):
                l += board[row][y:y + 3]
            if not legit_list(l):
                return False

    return True


def isValidSudokuFill(board: [[str]], row: int, col: int, fill_value: int) -> bool:

    if fill_value in board[row]:
        return False

    if fill_value in [row[col] for row in board]:
        return False

    i = row // 3
    j = col // 3
    x, y = i * 3, j * 3
    square = []
    for row in range(x, x + 3):
        square += board[row][y:y + 3]
    if fill_value in square:
        return False

    return True


def legit_list(l) -> bool:
    d = Counter(l)
    del d["."]
    return all(x == 1 for x in d.values())
