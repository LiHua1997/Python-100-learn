# # 练习1：输入一个正整数判断是不是素数。
# # 提示：素数指的是只能被1和自身整除的大于1的整数
# # 解法1：
# number = int(input('请输入一个整数\n'))
# is_prime = True
# for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print('是素数')
# else:
#     print('不是素数')
#
# # 解法2：
# from math import sqrt
#
# num = int(input('请输入一个正整数： '))
# end = int(sqrt(num))
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
#
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)
#

# 练习2 输入两个正整数，计算它们的最大公约数和最小公倍数。
"""
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
"""
# a = int(input('请输入正整数a： '))
# b = int(input('请输入正整数b： '))
# if a > b:
#     a, b = b, a
# for i in range(a, 0, -1):
#     if a % i == 0 and b % i == 0:
#         print("%d, %d最大公约数是：%d" %(a, b, i))
#         print("%d, %d最小公倍数是：%d" %(a, b, a * b // i)) #取模似乎没必要
#         break
# 解法2
a = int(input('请输入正整数a： '))
b = int(input('请输入正整数b： '))
if a > b:
    a, b = b, a
while a % b != 0:
    tem = a % b
    a = b
    b = tem
print(b)
# 练习3 打印三角形
# for i in range(1, 6):
#     print('*' * i)
# print()
# for i in range(1, 6):
#     print(' ' * (5 - i) + '*' * i)
# print()
# for i in range(1, 10, 2):
#     blank = int((9 - i) / 2)
#     print(blank * ' ' + '*' * i + blank * ' ')
# print()
# row = 5
# for i in range(row):
#     for _ in range(i + 1):
#         print("*", end='')
#     print()
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(" ", end="")
#         else:
#             print("*", end='')
#     print()
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(" ", end='')
#     for _ in range(2 * i + 1):
#         print("*", end='')
#     print()
