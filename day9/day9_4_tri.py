"""
计算三角形周长和面积

Version: 0.1
Author: St
"""
from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print("三角形的周长是", tri.perimeter())
        print("三角形的面积是", tri.area())
    else:
        print('这不是三角形')


if __name__ == '__main__':
    main()
