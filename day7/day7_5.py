"""
返回某年某月某日是一年的第几天

Version: 0.1
Author: St

"""


def is_leap_year(year):
    """
    判断某年是否是闰年
    :param year: 输入的年份
    :return: True表示是闰年 False表示不是闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """
    返回是一年中的第几天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 一年中的第几天
    """
    days = 0
    monthes = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    for i in range(month - 1):
        days += monthes[i]
    days += day
    return days


def main():
    year, month, day, = 2020, 2, 1
    print(which_day(year, month, day))


if __name__ == '__main__':
    main()
