def init_board(n: int):
    board = [[0] * (n) for i in range(n)]
    for line in (board[0], board[1]):
        for numbers in range((len(line))):
            line[numbers] = 2

    for line in (board[n - 2], board[n - 1]):
        for numbers in range((len(line))):
            line[numbers] = 1
    return board


def print_board(board: list[list[int]]):
    res = ""
    letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
               13: 'm', 14: 'n', 15: '0', 16: 'p', 17: 'q',
               18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'x'}
    x = len(board[0])
    y = 1
    n = len(board[0])
    res += "    "
    res += " —" * n
    res += " \n"
    for line in board:
        if x < 10:
            res += " " + str(x) + ' |'
        elif x >= 10:
            res += str(x) + ' |'
        for i in range(len(line)):
            if line[i] == 2:
                res += ' B'
            elif line[i] == 0:
                res += ' .'
            elif line[i] == 1:
                res += ' W'
        x -= 1
        res += " |" + "\n"

    res += "    "
    for j in range(n):
        res += " —"
    res += " \n"
    res += "    "
    for l in range(n):
        res += " " + letters.get(y)
        y += 1
    print(res)


def winner(board : list[list[int]]):
    win = None
    for line in (board[0],board[len(board)-1]):
        if 1 in board[0]:
            win = 1
        elif 2 in board[len(board)-1]:
            win = 2
    return win


def is_in_board(n : int,pos : tuple[int,int]):
    i = None
    j = None
    res = None
    if 0 <= pos[0] and pos[0] <n:
        i = True
    if 0 <= pos[1] and pos[1] < n:
        j = True

    if j == True and i == True:
        res = True
    else:
        res = False
    return res


def input_move():

    res = False
    while res != True:
        x = input("What's your next move?")
        if len(x) == 5:
            if x[0].islower() and x[1].isdigit() and x[2] == '>' and  x[3].islower() and x[4].isdigit():
                res = True
        elif len(x) == 6:
            if x[0].islower() and x[1].isdigit() and x[2] == '>' and x[3].islower() and x[4].isdigit()\
                    and x[5].isdigit():
                res = True
            elif x[0].islower() and x[1].isdigit() and  x[2].isdigit() and x[3] == '>' and x[4].islower()\
                   and x[5].isdigit():
                res = True

        elif len(x) == 7:
            if x[0].islower() and x[1].isdigit() and  x[2].isdigit() and x[3] == '>' and x[4].islower()\
                    and x[5].isdigit() and x[6].isdigit():
                res = True
    return x

print(input_move())
#pytest -v test_partie1.py