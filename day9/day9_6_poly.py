"""
函数的重写

version: 0.1
Author: St
"""

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """ 定义抽象类"""

    def __init__(self, nick_name):
        """
        初始化pet抽象类
        :param nick_name:名字
        """
        self._nick_name = nick_name

    @abstractmethod
    def make_voice(self):
        """定义叫声"""
        pass


class Dog(Pet):

    def make_voice(self):
        """狗叫"""
        print('%s:汪汪汪' % self._nick_name)


class Cat(Pet):

    def make_voice(self):
        """猫叫"""
        print('%s:喵喵喵' % self._nick_name)


def main():
    pets = [Dog('小花'), Cat('罗小黑'), Dog('旺财')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
