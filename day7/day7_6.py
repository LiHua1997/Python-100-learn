"""
杨辉三角

Version： 0.1
Author: St

"""


# def YangHui(rows):
#     """
#     生成杨辉三角
#     :param rows: 生成行数
#     :return:
#     """
#     t = []
#     for i in range(rows):
#         t.append([])
#         for j in range(i+1):
#             if j == 0 or j == i :
#                 t[i].append(1)
#             else:
#                 t[i].append(t[i - 1][j - 1] + t[i - 1][j])
#     return t

def YangHui(num):
    t = [[]] * num
    for row in range(len(t)):
        t[row] = [None] * int(row + 1)
        for col in range(row+1):
            if col == 0 or col == row:
                t[row][col] = 1
            else:
                t[row][col] = t[row - 1][col] + t[row - 1][col - 1]
    return t


print(YangHui(5))
