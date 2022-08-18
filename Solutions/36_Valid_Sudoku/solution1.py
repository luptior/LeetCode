from collections import Counter

"""
Runtime: 145 ms, faster than 56.31% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 35.29% of Python3 online submissions for Valid Sudoku.
"""


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        for row in board:
            if not self.no_repeat(row):
                return False

        for i in range(9):
            if not self.no_repeat([ board[j][i] for j in range(9)]):
                return False

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                count = set()
                for ii in range(i, i+3):
                    for jj in range(j, j+3):
                        if board[ii][jj] == ".":
                            continue
                        elif board[ii][jj] in count:
                            return False
                        else:
                            count.add(board[ii][jj])
        return True

    def no_repeat(self, l: [str]) -> bool:
        d = Counter(l)
        if "." in d:
            del d["."]

        return all([ v == 1 for v in d.values() ])


if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board2))
