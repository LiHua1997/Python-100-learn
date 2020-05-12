"""
判断素数

Version = 0.1
Author = St

"""
import math


# def is_prime(num):
#     is_prime = True
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print('%d是素数' % num)
#     else:
#         print('%d不是素数' % num)
#
#
# if __name__ == '__main__':
#     num = int(input('请输入数字： '))
#     is_prime(num)


# answer
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    num = int(input('请输入数字： '))
    if is_prime(num):
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)
