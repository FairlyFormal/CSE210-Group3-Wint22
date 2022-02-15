import Words
from Terminal_Butler import Terminal
import Stickman


#RESPONSIBILITIES:
# Starts the game, Ends the game, Communicated with Terminal to determine the end of the game.

#Start game - Initialize the three classes (Word, stickman, and terminal).

#Ends Game - Once a guess has been made the Terminal will check every turn to see if the guess affects lives or if the word has been guessed.


class Commander():


    def __init__(self):
        self.terminal = Terminal()
        pass


    
    def start_game(self): #Initializes all the processes from the different classes.

        Terminal.print_hidden_word()
        #Prints the hidden word in _____ underscores.
        Stickman.draw_stickman() #Draws the stickman.
        Terminal.user_guess #Prompts the user to input a letter.


    def end_game(self): #Checks with terminal to see if user has guessed the word or has lost all their lives.

        print('Thanks for playing.')


