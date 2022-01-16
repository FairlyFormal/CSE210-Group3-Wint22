'''
Solo Checkpoint 02
Author: Bro. Hayes
'''

from operator import truediv
from turtle import Turtle


def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player
    player = 'x'

    # create a board
    board = create_board()

    # loop if there isn't a winner or if the game isn't a draw
    while not is_draw(board) and not is_winner(board):
        # display the board
        display_board(board)
        # allow the player to make a move
        make_move(player,board)
        # pick the next player
        player = next_player(player)

    # display the final board
    display_board(board)
    # show message for winner and thanks for playing
    endgame(is_winner(board), player)
    pass

def endgame(winner, player):

    if not winner:
        print()
        print('It\'s a draw!')
    else:
        print()
        print(f'Player {next_player(player)} won.')

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for square in range(9):
        board.append(square+1)
    return board
'''
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9
'''

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    pass

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    value = 0
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            value = value
        else:
            value += 1
    if value == 9:
        return True
    else:
        return False

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    #check if rows or columns or diagonals are matching values
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    #maybe try doing some try: except: stuff
    try:
        print()
        number = int(input(f'Player {player} What square would you like to go in? '))-1
        if board[number] == 'x' or board[number] == 'o' or number > 8:
            print('That is not a valid move. Try another space.')
            make_move(player, board)
        else:
            board[number] = player
            return
    except:
        print('Please enter a number between 1 and 9.')
        make_move(player, board)
    pass      

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == 'x':
        return 'o'
    else:
        return 'x'

# run main if this has been called from the command line
if __name__ == "__main__":
    main()