class Solution:
    def maximalRectangle(self, matrix) -> int:
        nr = len(matrix)

        if nr == 0:
            return 0

        nc = len(matrix[0])

        if nc == 0:
            return 0

        def search(to_right, to_bottom, rect):

            new_rect = rect[:]

            right = []
            if rect[3] < nc - 1 and to_right:
                for x in range(rect[0], rect[2] + 1):
                    right.append(matrix[x][rect[3] + 1])
            else:
                right.append("0")
            bottom = []
            if rect[2] < nr - 1 and to_bottom:
                for y in range(rect[1], rect[3] + 1):
                    bottom.append(matrix[rect[2] + 1][y])
            else:
                bottom.append("0")
            corner = "0"

            if rect[3] < nc - 1 and rect[2] < nr - 1 and to_right and to_bottom:
                corner = matrix[rect[2] + 1][rect[3] + 1]

            if "0" in right and "0" in bottom:
                return False, False, rect

            else:

                if not "0" in bottom:
                    new_rect1 = new_rect[:]
                    new_rect1[2] += 1
                    to_right1, to_bottom1, result1 = search(False, True, new_rect1)
                    while to_right1 or to_bottom1:
                        to_right1, to_bottom1, result1 = search(to_right1, to_bottom1, result1)
                    lot1 = (result1[3] + 1 - result1[1]) * (result1[2] + 1 - result1[0])
                else:
                    lot1 = 0

                if "0" not in right:
                    new_rect2 = new_rect[:]
                    new_rect2[3] += 1

                    to_right2, to_bottom2, result2 = search(True, False, new_rect2)
                    while to_right2 or to_bottom2:
                        to_right2, to_bottom2, result2 = search(to_right2, to_bottom2, result2)

                    lot2 = (result2[3] + 1 - result2[1]) * (result2[2] + 1 - result2[0])
                else:
                    lot2 = 0

                if "0" not in right and "0" not in bottom and corner != "0":
                    new_rect3 = new_rect[:]
                    new_rect3[2] += 1
                    new_rect3[3] += 1

                    # print(rect[0], rect[1], "new_rect3", new_rect3)
                    to_right3, to_bottom3, result3 = search(True, False, new_rect3)
                    while to_right3 or to_bottom3:
                        to_right3, to_bottom3, result3 = search(to_right3, to_bottom3, result3)
                    lot3 = (result3[3] + 1 - result3[1]) * (result3[2] + 1 - result3[0])
                else:
                    lot3 = 0

                # print(rect[0], rect[1], "new_rect1", new_rect1)
                # print(rect[0], rect[1], "new_rect2", new_rect2)

                # print(rect[0], rect[1], "result1", result1)
                # print(rect[0], rect[1], "result2", result2)
                # print(rect[0], rect[1], "result3", result3)

                mm = max(lot1, lot2, lot3)
                if lot1 == mm:
                    print(rect[0], rect[1], "result1", result1)
                    return False, False, result1
                elif lot2 == mm:
                    print(rect[0], rect[1], "result2", result2)
                    return False, False, result2
                else:
                    print(rect[0], rect[1], "result3", result3)
                    return False, False, result3

        maxi = 0

        for row in range(nr):
            for col in range(nc):

                if matrix[row][col] == "1":

                    rect = [row, col, row, col]  # left top x, y, right bootom x, y

                    to_right = True and rect[3] < nc - 1
                    to_bottom = True and rect[2] < nr - 1

                    _, _, result = search(to_right, to_bottom, rect)

                    lot = (result[3] + 1 - result[1]) * (result[2] + 1 - result[0])
                    print(result, lot)

                    if lot > maxi:
                        maxi = lot

        return maxi
