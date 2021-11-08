def init_board(n : int):
    board = [[0] * (n) for i in range(n)]
    for line in (board[0], board[1]):
        for numbers in range((len(line))):
                line[numbers] = 2

    for line in (board[n - 2], board[n-1]):
        for numbers in range((len(line))):
                line[numbers] = 1
    return board
def print_board(board : list[list[int]]):

    res=""
    for line in board:
        for i in range(len(line)):
            if line[i] == 2:
                res += 'B '
            elif line[i] == 0:
                res += '. '
            elif line[i] == 1:
                res += 'W '
        res +="\n"
    return res

print(init_board(8))
print(print_board(init_board(8)))



