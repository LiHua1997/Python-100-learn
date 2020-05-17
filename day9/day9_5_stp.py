"""
类的继承

Version: 0.1
Author: St
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch_tv(self):
        if self._age > 18:
            print('%s正在观看岛国大片' % self._age)
        else:
            print('%s正在观看熊出没' % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teaching(self, course):
        print("%s%s正在教%s" % (self._title, self._name, course))


def main():
    st = Teacher('宋拓', 18, '菜鸡')
    st.title = '砖家'
    st.watch_tv()
    print(st.title)


if __name__ == '__main__':
    main()
