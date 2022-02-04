#STEPS OF THE GAME (IN ORDER):

# 0. Ensures objects interact correctly | Commander()

# 1. Displays the hidden word at the top of the console. | Words()
# 2. Displays the full stickman. | Stickman()
# 3. Displays input prompt for user. | Commander()

# 4. Processes player input through logic within Terminal | Terminal()
# 4A. If input is invalid, throws an error | Terminal()
# 4B. If input is valid, checks input with random word.  | Words()

# 6A. If word is correct, reveals word on console. | Words()
# 6B. If word is incorrect, takes a life from stickman. | Stickman()

# 7A. Checks if stickman has all lives | Stickman()
# 7B. Checks if word is complete | Words()

# 8. End game screen. (Win or Lose) | Commander()


#================================================================================================================================


class Commander():

    #responsibilities: start game, show board

    def __init__(self):

        pass

    def start_game():

        print('Welcome to the game, here\'s the word: ')
        #Prints the stickman from the stickman object.
        #Words() Prompts user
    
    pass

class Stickman():


    #responsibilities: list of lines, keep track of lives

    pass

class Words():


    #responsibilities: keep list of words, pick random word, keep random word private, ask input from user

    pass

class Terminal():


    #responsibilities: error handling, run inputs (check its a letter - not a number or unkown symbol)

    pass


#================================================================================================================================

#call objects here: