"""
Runtime: 28 ms, faster than 89.73% of Python3 online submissions for Valid Tic-Tac-Toe State.
Memory Usage: 14.2 MB, less than 91.44% of Python3 online submissions for Valid Tic-Tac-Toe State.
"""


from collections import Counter


class Solution:
    def validTicTacToe(self, board: [str]) -> bool:

        d = Counter(board[0])
        d += Counter(board[1])
        d += Counter(board[2])

        print(d)

        if d["O"] > d["X"] or d["X"] - d["O"] > 1:
            return False

        if self.if_win(board, "O") and d["X"] > d["O"]:
            return False

        if self.if_win(board, "X") and not d["X"] > d["O"]:
            return False

        return True

    def if_win(self, board: [str], symbol) -> bool:

        if board[0] == f"{symbol}" * 3 or board[1] == f"{symbol}" * 3 or board[2] == f"{symbol}" * 3 or \
                all([board[i][0] == symbol for i in range(3)]) or \
                all([board[i][1] == symbol for i in range(3)]) or \
                all([board[i][2] == symbol for i in range(3)]) or \
                all([board[i][i] == symbol for i in range(3)]) or \
                all([board[i][2 - i] == symbol for i in range(3)]):
            return True
        else:
            return False

