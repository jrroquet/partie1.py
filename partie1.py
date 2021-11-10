"""
Name: Roquet
Firstname: Ghislain
Serial number: 000539192
Section: B1-INFO
Input: "n" = Size of the board, then each player type is move.
Output: The player who won the game
"""

letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
           13: 'm', 14: 'n', 15: '0', 16: 'p', 17: 'q',
           18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'x'}


# Global dict because I use it many times

def init_board(n: int):
    """create the board and change the values of the first two and last lines in 2 and 1."""
    board = [[0] * (n) for _ in range(n)]
    for line in (board[0], board[1]):
        for numbers in range((len(line))):
            line[numbers] = 2

    for line in (board[n - 2], board[n - 1]):
        for numbers in range((len(line))):
            line[numbers] = 1
    return board


def print_board(board: list[list[int]]):
    res = ""

    x = len(board[0])
    y = 1
    n = len(board[0])
    res += "    "
    res += " —" * n
    res += " \n"
    for line in board:
        if x < 10:  # For the space bc there's one other when x < 10
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
    for j in range(n):  # n and not x because x changed of value in the for_loop
        res += " —"
    res += " \n"
    res += "    "
    for letter in range(n):
        res += " " + letters.get(y)
        y += 1
    print(res)


def winner(board: list[list[int]]):
    """Tell if someone win the game or not"""
    win = None
    for _ in (board[0], board[len(board) - 1]):  # look if there is a "1" in the first 'black' line
        if 1 in board[0]:
            win = 1
        elif 2 in board[len(board) - 1]:  # look if there is a "2" in the first 'white' line
            win = 2
    return win


def is_in_board(n: int, pos: tuple[int, int]):
    """check if the move stay in the board or not"""
    i, j, res = None, None, None

    if 0 <= pos[0] < n:  # if the move is in the board, pos[0] and pos[1] have to be between 0 and n
        i = True
    if 0 <= pos[1] < n:
        j = True

    if j is True and i is True:
        res = True
    else:
        res = False
    return res


def input_move():
    """The player type is move. The program continue to ask for a move until the one that was written is in the
     correct "form" (example: a2>a3, a12>b11, a10>b9, a9>b10) """
    global x
    res = False

    while not res:
        x = input("")
        if len(x) == 5:  # check in case len(move) == 5 example: a2>a3
            if x[0].islower() and x[1].isdigit() and x[2] == '>' and x[3].islower() and x[4].isdigit():
                res = True

        elif len(x) == 6:  # check in case len(move) == 6 example: a10>a9 & a9>a10
            if x[0].islower() and x[1].isdigit() and x[2] == '>' and x[3].islower() and x[4].isdigit() \
                    and x[5].isdigit():
                res = True
            elif x[0].islower() and x[1].isdigit() and x[2].isdigit() and x[3] == '>' and x[4].islower() \
                    and x[5].isdigit():
                res = True

        elif len(x) == 7:  # check in case len(move) == 7 example: a12>a13
            if x[0].islower() and x[1].isdigit() and x[2].isdigit() and x[3] == '>' and x[4].islower() \
                    and x[5].isdigit() and x[6].isdigit():
                res = True
        print("Invalid Move. Please try again.")
    return x


def extract_pos(n: int, str_pos: str):
    """Allow to have a tuple of coordinates from player's actual position and player's next position"""
    res, j, i, str_pos_1_2 = None, None, n, None
    if len(str_pos) <= 3:  # str_pos cannot be longer than 3 bc there's a maximum of 26 lines so 1 letter + 2 numbers
        for key, value in letters.items():
            if str_pos[0] == value:
                j = key - 1
        if len(str_pos) == 3:  # give a tuple when player's move go to a 2 numbers line
            str_pos_1_2 = str_pos[1] + str_pos[2]
            str_pos_1_2 = int(str_pos_1_2)
            i -= str_pos_1_2
        elif len(str_pos) == 2:  # give a tuple when player's move go to a 2 numbers line
            i -= int(str_pos[1])
        if is_in_board(n, (j, i)):  # check if the tuple is in the board or not, if it's True it return res
            res = (i, j)
    return res


def check_move(board: list[list[int]], player: int, str_move: str):
    """Check if player's move respects the game's rules"""
    res, sign, x = False, str_move.index('>'), len(board)  # index give the where the sign is as an int
    movement = (str_move[sign:].replace('>', ''), str_move[:sign])
    # replace delete the sign, we take what is before and after it
    movement = (extract_pos(x, movement[0]), extract_pos(x, movement[1]))
    # extract_pos give the coordinates of the two positions
    if player == 1:
        if board[movement[1][0]][movement[1][1]] == 1:  # check if initial_position is piece or a empty case
            if movement[0][0] < movement[1][0]:  # check if player don't try to go backward
                if board[movement[0][0]][movement[0][1]] == 0:  # if empty case, no problem player can go ahead
                    if abs(movement[0][0] - movement[1][0]) == 1 and (abs(movement[0][1] - movement[1][1]) == 1
                                                                      or abs(movement[0][1] - movement[1][1]) == 0):
                        # check if player's move go ahead or in diagonal 1 line above
                        res = True
                if board[movement[0][0]][movement[0][1]] == 2:  # if the case is not empty, player can't go ahead
                    if abs(movement[0][0] - movement[1][0]) == 1 and abs(movement[0][1] - movement[1][1]) == 1:
                        # check if player's move go in diagonal 1 line above
                        res = True
    if player == 2:  # follow the same pattern but it's one line below
        if board[movement[1][0]][movement[1][1]] == 2:
            if movement[1][0] < movement[0][0]:
                if board[movement[0][0]][movement[0][1]] == 0:
                    if abs(movement[1][0] - movement[0][0]) == 1 and (abs(movement[1][1] - movement[0][1]) == 1
                                                                      or abs(movement[1][1] - movement[0][1]) == 0):
                        res = True
                if board[movement[0][0]][movement[0][1]] == 1:
                    if abs(movement[1][0] - movement[0][0]) == 1 and abs(movement[1][1] - movement[0][1]) == 1:
                        res = True
    return res


def play_move(board: list[list[int]], move: tuple[tuple[int, int], tuple[int, int]], player: int):
    """Suppose that check_move is ok, play_move change the board with different player's moves"""
    pos_init, end_pose = move[0], move[1]  # just making writing and reading easier
    if player == 1:  # in board, put a 0 were the player was, put a 1 were he is now and initialize the new init_pos
        board[pos_init[0]][pos_init[1]] = 0
        board[end_pose[0]][end_pose[1]] = 1
        pos_init = end_pose

    if player == 2:  # in board, put a 0 were the player was, put a 2 were he is now and initialize the new init_pos
        board[pos_init[0]][pos_init[1]] = 0
        board[end_pose[0]][end_pose[1]] = 2
        pos_init = end_pose
    print_board(board)  # print the new board with the move made
    return


def main(n):
    """Take all the function above in one big function and start the game when we call it
     (idk if we say call like in french but it's nothing)"""
    board = init_board(n)
    print_board(board)
    count = 1

    while winner(board) is None:  # loop that re-ask for a move since there's a winner

        if count == 1:
            player = 1

        else:
            player = 2

        print("Player", player, "what's your next move?")
        move = input_move()  # player type his move

        if check_move(board, player, move):  # if the move respect the rules, can be played
            sign = move.index('>')
            movement = (move[:sign], move[sign:].replace('>', ''))
            movement = (extract_pos(n, movement[0]), extract_pos(n, movement[1]))  # the same in check_move
            play_move(board, movement, player)  # change board and print the new one
            count = (count + 1) % 2  # if rest of the div == 1, it's player one, if rest == 0, it's player two
    print("And the winner is...Player", winner(board), "! \n", "Congratulation!!")  # lil' message for the winner


if __name__ == '__main__':
    print("Size of the board?")
    n = int(input())
    print(main(n))

# DS cmd ==> cd C:\Users\Junior\PycharmProjects\Projet_ANNEE then python3 partie1.py
