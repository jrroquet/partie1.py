def main(n):
    board = [[0] * (n + 3) for i in range(n + 3)]

    def board_mat(x):
        for line in (x[0], x[len(x) - 1]):
            for numbers in range((len(line))):
                if numbers in (0, 1, len(line) - 2, len(line) - 1):
                    line[numbers] = ''

        for line in (x[1], x[2]):
            for numbers in range((len(line))):
                if numbers in (0, 1, len(line) - 1):
                    line[numbers] = 0
                else:
                    line[numbers] = 2

        for line in (x[n - 1], x[n]):
            for numbers in range((len(line))):
                if numbers in (0, 1, len(line) - 1):
                    line[numbers] = 0
                else:
                    line[numbers] = 1
        return x

    def print_board(x):
        res = ""
        for line in x:
            for i in range(len(line)):
                if line[i] == 2:
                    res += 'B '

                elif line[i] == 0:
                    res += '. '

                else:
                    res += 'W '
            res += "\n"

        return res

    return print_board(board_mat(board))


print(main(8))
