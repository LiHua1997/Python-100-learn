"""
斐波那契数列
斐波那契数列（Fibonacci sequence），又称黄金分割数列，
是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为"兔子数列"。斐波那契数列的特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

Version: 0.1
Author: St
"""

first = 1
mid = 1
for i in range(1,21):
    if i <= 2:
        print("1")
    else:
        new = first + mid
        first = mid
        mid = new
        print(new)
# 答案：
# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a+b
#     print(a)