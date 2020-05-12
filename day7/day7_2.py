"""
验证码生成
随机生成大小写字母和数字组成的指定长度验证码

Version = 0.1
Author = St

"""
import random


def generate(lenth):
    key_words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codes = ''
    for _ in range(lenth):
        codes += key_words[random.randint(0, len(key_words))]
    return codes


def main():
    lenth = int(input('请输入验证码长度： '))
    print('生成的验证码为： ' ,generate(lenth))


if __name__ == '__main__':
    main()
