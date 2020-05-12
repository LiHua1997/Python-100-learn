"""
判断回文素数

Version: 0.1
Author: St

"""

from day6_3 import is_prime
from day6_2 import is_palindrome

if __name__ == '__main__':
    num = int(input('请输入数字：'))
    if is_prime(num) and is_palindrome(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)
