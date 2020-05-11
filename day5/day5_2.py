"""
完美数
说明：完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
完美数有很多神奇的特性，有兴趣的可以自行了解。

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