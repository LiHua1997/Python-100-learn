"""
获取文件后缀名

Version = 0.1
Author = St

"""


def get_name(file_name, has_dot=False):
    """
    获取后缀名
    :param file_name: 文件名
    :param has_dot: 是否带点
    :return:后缀名
    """
    pos = file_name.rfind('.')
    if 0 < pos < len(file_name):
        index = pos if has_dot == True else pos + 1
        return file_name[index:]
    else:
        return ''


def main():
    file_name = 'study.txt'
    print(get_name(file_name, True))


if __name__ == '__main__':
    main()
