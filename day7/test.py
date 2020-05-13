import os


def show_board(board):
    print(board['A1'] + ' | ' + board['A2'] + ' | ' + board['A3'])
    print('--+---+--')
    print(board['B1'] + ' | ' + board['B2'] + ' | ' + board['B3'])
    print('--+---+--')
    print(board['C1'] + ' | ' + board['C2'] + ' | ' + board['C3'])


def set_chess(num, init_board):
    current_board = init_board
    if num % 2 == 0:
        print('玩家1：x')
        pos = input('请输入位置')
        os.system('clear')
        current_board[pos] = 'x'
    else:
        print('玩家2：o')
        pos = input('请输入位置')
        os.system('clear')
        current_board[pos] = 'o'b
    return current_board

def main():
    init_board = {
        'A1': ' ', 'A2': ' ', 'A3': ' ',
        'B1': ' ', 'B2': ' ', 'B3': ' ',
        'C1': ' ', 'C2': ' ', 'C3': ' '
    }

    show_board(init_board)
    counter = 0
    while counter < 9:
        current_board = set_chess(counter, init_board)
        show_board(current_board)
        counter += 1


main()
