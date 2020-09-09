import random
#Playing board


def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)

#Player input


def player_input():
    marker = ''

    while marker != "X" and marker != "O":
        marker = input("Player1: Choose X or O: ").upper()
    if marker == "X":
        return("X", "O")
    else:
        return("O", "X")

player1, player2 = player_input()
print(player1)
print(player2)

#Place marker on board


def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, "T", 8)
display_board(test_board)

#Check if there is a winner


def win_check(board, mark):
    #Win Tic Tac Toe
    #All Rows and see if they match
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or

            #Check columns to see if they match
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            #Check both diagonals

            (board[3] == mark and board[5] == mark and board[7] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark)
            )

print(win_check(test_board, "X"))

#Which player goes first


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

print(choose_first())