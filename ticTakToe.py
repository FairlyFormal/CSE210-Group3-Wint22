'''
Solo Checkpoint 02
Author: Bro. Hayes
'''

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

    # create a board

    # loop if there isn't a winner or if the game isn't a draw

        # display the board

        # allow the player to make a move

        # pick the next player

    # display the final board

    # show message for winner and thanks for playing
    pass

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
    print(f"{board[3]}|{board[4]}|{board[2]}")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    pass

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
    pass

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    #check if rows or columns or diagonals are matching values
    return (
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
    )
    pass

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    #maybe try doing some try: except: stuff
    pass      

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    
    pass

# run main if this has been called from the command line
if __name__ == "__main__":
    main()