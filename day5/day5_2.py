"""
完美数
找出1，9999之间的完美数
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

Version: 0.1
Author: St
"""

for num in range(1,10001):
    factors_list = []
    for factor in range(1, num):
        if num % factor == 0:
            factors_list.append(factor)
    if sum(factors_list) == num:
        print(num)
#总结，时间复杂度太差
# 答案
# from math import sqrt
#
# for num in range(1, 10001):
#     result = 0
#     for factor in range(1, int(sqrt(num) + 1)):
#         if num % factor == 0:
#             result += factor
#             if factor> 1 and num // factor != factor:
#                 result += num//factor
#     if result == num:
#         print(num)