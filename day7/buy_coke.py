"""
买可乐
输入买的总数，以及多少个空瓶可以换一瓶，输出能喝到的可乐数

Version:0.1
Author:St

"""


def buy_cock(num, flag):
    """输入买可乐，记录获得的可乐总数，剩余空瓶数，借来的可乐，交换来的可乐"""
    total = 0
    empty = 0
    borow = 0
    change = 0
    for _ in range(num):
        total += 1
        empty += 1
        if empty == flag:
            total += 1
            empty += 1
            empty -= flag
            change += 1
    if empty == flag - 1:
        total += 1
        borow += 1
        empty += 1
        empty = 0
    return total, empty, borow, change


if __name__ == '__main__':
    num = int(input('买几瓶： '))
    flag = int(input('几瓶换一个： '))
    total, empty, borow, change = buy_cock(num, flag)
    print("总共可获得%d瓶，其中兑换了%d瓶，借了%d瓶，剩%d个空瓶子" % (total, change, borow, empty))
