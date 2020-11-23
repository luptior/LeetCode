def sumRegion(matrix, row1: int, col1: int, row2: int, col2: int) -> int:
    result = 0

    for i in range(row1, row2 + 1):
        result += sum(matrix[i][col1: col2 + 1])

    return result

"""
3.largest sub grid——给一个grid和maxSum，求最大边长k，使grid中所有k * k subgrid的sum都<maxSum
这道题分为2部分吧，第一部分是找grid中k * k subgrid的maxsum，这就是dp, 造一个新grid, 每个元素是0,0到i,j所有元素和然后遍历grid, 每个subgrid的和都能在constant算出来，leetcode有原题
第二部分是在0到Min(m,n)间找到最大k，就是触下界的二分法
"""


if __name__ == '__main__':
    grid = [[1,1,1], [1,1,1], [1,1,1]]
    maxCapacity = 4