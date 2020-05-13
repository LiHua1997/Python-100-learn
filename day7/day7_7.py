"""
双色球抽奖
输入注数，输出几个由6个（1，34）和1个（1，16）的数字构成的双色球彩票

Version = 0.1
Author = St
"""

from random import randrange, randint, sample


def select_balls():
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls += sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))

    return selected_balls


# def display_balls(balls):
#     for index in range((len(balls))):
#         if index == 6:
#             print('|', end=' ')
#         print(balls[index], end=' ')

def display_balls(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print("%02d" % ball, end=' ')


def main():
    num = int(input('机选几注： '))
    for _ in range(num):
        balls = select_balls()
        display_balls(balls)
        print()


if __name__ == '__main__':
    main()
