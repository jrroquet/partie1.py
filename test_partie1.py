from partie1 import *

def test_print_board():
    from contextlib import redirect_stdout
    from io import StringIO
    board = [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    with StringIO() as buffer, redirect_stdout(buffer):
        print_board(board)
        _buffer = str(buffer.getvalue())
    expected_with_edges = '     — — — — — \n\
 5 | B B B B B |\n\
 4 | B B B B B |\n\
 3 | . . . . . |\n\
 2 | W W W W W |\n\
 1 | W W W W W |\n\
     — — — — — \n\
     a b c d e'

    assert _buffer.strip() == expected_with_edges.strip()


def test_init_board():
    n = 9
    board = init_board(n)    
    expected = [[2]*n]*2 + [[0]*n]*(n-4) + [[1]*n]*2    
    assert board == expected, 'Initiliasation plateau incorrecte'


def test1_winner():    
    error = ""
    n = 9        
    # Player 1  : row = 0
    for i in range(0,n) :
        board = init_board(n)
        board[0][i] = 1
        if not winner(board) == 1: 
            error = 'Pion blanc sur la case [O,{}] —> winner = 1'.format(i)
            break
    assert error == "", error 

def test2_winner():    
    error = ""
    n = 8        
        
    # Player 1 : row = 1
    board = init_board(n)
    for i in range(n):
        board[1][i] = 1
        if not winner(board) == None: 
            error = 'Pion blanc sur la case [1,{}] mais pas en [0,{}] —> winner = None'.format(i,i)
            break
    assert error == "", error         

def test3_winner():    
    error = ""
    n = 10        

    # Player 2 : row = n-1
    for i in range(n) :
        board = init_board(n)
        board[-1][i] = 2
        if not winner(board) == 2: 
            error = 'Pion noir sur la case [{},{}] —> winner = 2'.format(n-1,i)
            break
    assert error == "", error         

def test4_winner():    
    error = ""
    n = 6        

    # Player 2 : row = n-2
    board = init_board(n)
    for i in range(n):
        board[-2][i] = 2
        if not winner(board) == None: 
            error = 'Pion noir sur la case [{},{}] mais pas en [{},{}] —> winner = None'.format(n-2,i,n-1,i)
            break
    assert error == "", error         

    
def test_is_in_board():
    error = ''
    n = 8
    board = [ [ 0 for j in range (n) ] for i in range(n) ]
    stop = False

    # Tests positions 
    for i in range (-1,n+1):
        for j in range(-1, n+1) :
            if not is_in_board(n, (i,j)) == ((0 <= i < n) and (0 <= j < n)):
                error = 'Erreur pour paire (' +str(i)+','+str(j)+')'
                stop = True
                break
        if stop:
            break

    assert error == "", error         
                
def test_input_move(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "aa2>b2")
    monkeypatch.setattr('builtins.input', lambda _: "a1>b1")
    res = input_move()
    assert res == "a1>b1"

    
def test_extract_pos():
    error = ''
    n = 7
    board = [ [ 0 for j in range (n) ] for i in range(n) ]
    
    
    pos = ['a7','a6','b7','a1','a2','b1']
    res = [(0,0),(1,0),(0,1),(n-1,0),(n-2,0),(n-1,1)]

    for i in range(len(pos)) :
        if not extract_pos(n, pos[i]) == res[i]: 
            error = 'La position {} devrait correspondre à la paire d indices {}.'.format(pos[i],res[i])
            break

    assert error == "", error         

def test1_check_move():
    board = [
        [2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    res = check_move(board, 2, 'd4>d3')    
    assert res == False, "Erreur dans vérification des règles"

def test2_check_move():
    board = [
        [2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 0, 2, 2, 2],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    res = check_move(board, 2, 'c2>d4')    
    assert res == False, "Erreur dans vérification des règles"

def test3_check_move():
    board = [
        [2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 0, 2, 2, 2],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    res = check_move(board, 1, 'c2>d3')    
    assert res == True, "Erreur dans vérification des règles"

def test4_check_move():
    board = [
        [2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 0, 2, 2, 2],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    res = check_move(board, 2, 'c2>c3')    
    assert res == False, "Erreur dans vérification des règles"


def test5_check_move():
    board = [
        [2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 0, 2, 2, 2],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    res = check_move(board, 2, 'd3>d4')    
    assert res == False, "Erreur dans vérification des règles"



def test_play_move():
    board = [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]

    play_move(board, ((3,0),(2,0)), 1)
    play_move(board, ((2,0),(1,1)), 1)
    play_move(board, ((1,2),(2,2)), 2)
    play_move(board, ((2,2),(3,3)), 2)

    print_board(board)

    expected = [
        [2, 2, 2, 2, 2],
        [2, 1, 0, 2, 2],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 2, 1],
        [1, 1, 1, 1, 1]
    ]

    assert board == expected, "Erreur dans l'execution des coups"
