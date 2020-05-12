"""
返回列表中的最大数和第二大数

Version = 0.1
Author = St

"""


# def get_max(list):
#     max = list[0]
#     for num in list:
#         max = num if num > max else max
#     return max


def main():
    list = [1, 3, 8, 4, 6, 78]
    # biggest = get_max(list)
    # list.remove(biggest)
    # second = get_max(list)
    (biggest, second) = get_max2(list)
    print("最大的数是%d， 第二大的数是%d" % (biggest, second))

#answer
def get_max2(list):
    m1, m2 = (list[0], list[1]) if list[0] > list[1] else (list[1], list[0])
    for num in list:
        if num > m1:
            m2 = m1
            m1 = num
        elif num > m2:
            m2 = num
    return m1, m2


if __name__ == '__main__':
    main()
