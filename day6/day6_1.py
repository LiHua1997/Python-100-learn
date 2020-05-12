"""
最小公倍数和最大公约数
输入两个数，得到他们的最小公倍数和最大公约数

Version: 0.1
Author: St

"""


def gcd(bigger, smaller):
    """求最大公约数"""
    if bigger < smaller:  # (bigger, smaller) = (smaller, bigger) if smaller >bigger else(bigger, smaller)
        bigger, smaller = smaller, bigger
    while bigger % smaller != 0:
        tem = bigger % smaller
        bigger = smaller
        smaller = tem
    return smaller


def lcm(bigger, smaller):
    """求最小公倍数"""
    return bigger * smaller // gcd(bigger, smaller)


if __name__ == '__main__':
    a = int(input("请输入a： "))
    b = int(input('请输入b： '))
    print('%d和%d的最大公约数为： %d\n%d和%d的最小公倍数为： %d' % (a, b, gcd(a, b), a, b, lcm(a, b)))
