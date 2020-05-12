"""
跑马灯

Version = 0.1
Author = St

"""

import os
import time


def light(content):
    """滚动播出content的内容"""
    while True:
        print(content)
        time.sleep(0.2)
        os.system('clear')
        content = content[1:] + content[0]


def main():
    content = input('输入跑马灯内容')
    light(content)


if __name__ == '__main__':
    main()
