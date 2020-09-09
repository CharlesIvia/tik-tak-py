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


def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, "T", 8)
display_board(test_board)