"""
move point

version = 0.1
author = St
"""
import math


class Point(object):
    """移动点"""

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self._x = x
        self._y = y

    def move_to(self, x, y):
        """
        通过指定坐标来移动
        :param x: 指定的横坐标
        :param y: 指定的纵坐标
        :return: 移动后的坐标
        """
        self._x = x
        self._y = y
        return self._x, self._y

    def move_by(self, dx, dy):
        """
        通过增加数值来移动
        :param dx: 横坐标增量
        :param dy: 纵坐标增量
        :return: 移动后的坐标
        """
        self._x += dx
        self._y += dy
        return self._x, self._y

    def distance(self, other_point):
        """
        计算两点之间的距离
        :param other_point: 另一个点
        :return: 两点间的距离
        """
        dx = self._x - other_point._x
        dy = self._y - other_point._y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)'%(str(self._x), str(self._y))



def main():
    point_a = Point(1, 1)
    point_b = Point(3, 3)
    print(point_a)
    print(point_a.move_to(3, 3))
    print(point_a.move_by(1,1))
    print(point_a.distance(point_b))

if __name__ == '__main__':
    main()
