"""
You are given an NxN chessboard, and you are required to place N queens on this chessboard such that no queen
is under threat from any other queen.

In chess a queen can move any number of steps horizontally, vertically, or diagonally.
This means that no queen should share a row, column, or diagonal with another queen.

from: https://www.educative.io/courses/dynamic-programming-in-python/q2nZmnkwGZD
"""


def isSafe(i, j, board):
    for c in range(len(board)):
        for r in range(len(board)):
            # check if i,j share row with any queen
            if board[c][r] == 'q' and i == c and j != r:
                return False
            # check if i,j share column with any queen
            elif board[c][r] == 'q' and j == r and i != c:
                return False
            # check if i,j share diagonal with any queen
            elif (i + j == c + r or i - j == c - r) and board[c][r] == 'q':
                return False
    return True


def nQueens(n, r, board):
    for r in range(len(board)):
        


def placeNQueens(n, board):
    # too place n queens on the table

    return nQueens(n, 0, board)[1]


if __name__ == '__main__':
    n = 4
    board = [["-" for _ in range(n)] for _ in range(n)]
    qBoard = placeNQueens(n, board)
    qBoard = "\n".join(["".join(x) for x in qBoard])
    print(qBoard)
