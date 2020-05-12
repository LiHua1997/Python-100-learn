"""
判断回文数
如 121 1234321

Version = 0.1
Author = St

"""


def is_palindrome(num):
    temp = num
    new = 0
    while temp > 0:
        new = new * 10 + temp % 10
        temp = temp // 10
    return num == new


if __name__ == '__main__':
    num = int(input('请输入数字： '))
    if is_palindrome(num):
        print('%d是回文数' % num)
    else:
        print('%d不是回文数' % num)
