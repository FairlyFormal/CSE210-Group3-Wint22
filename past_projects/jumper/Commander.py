import Words
<<<<<<< HEAD
from Terminal_Butler import Terminal
from Stickman import Stickman
=======
import Terminal_Butler
import Stickman
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06




<<<<<<< HEAD
#RESPONSIBILITIES:
# Starts the game, Ends the game, Communicated with Terminal to determine the end of the game.

#Start game - Initialize the three classes (Word, stickman, and terminal).

#Ends Game - Once a guess has been made the Terminal will check every turn to see if the guess affects lives or if the word has been guessed.


=======
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06
class Commander():


    def __init__(self):
<<<<<<< HEAD
        self.terminal = Terminal()
        self.stickman = Stickman()
        pass


    
    def start_game(self): #Initializes all the processes from the different classes.

        self.terminal.print_hidden_word()
        #Prints the hidden word in _____ underscores.
        self.stickman.draw_stickman() #Draws the stickman.
        self.terminal.user_guess #Prompts the user to input a letter.


    def end_game(self): #Checks with terminal to see if user has guessed the word or has lost all their lives.

        print('Thanks for playing.')


=======

        self.terminal = Terminal_Butler.Terminal()
        self.stickman = Stickman.Stickman()
        self.words = Words.Words()
        self.input = ''
        self.inplay = True
        self.lost = False



    
    def game_loop(self):

        while self.inplay:

            self.terminal.print_guessed_word(self.words.guessed_word)
            self.stickman.draw_stickman()
            self.get_input()
            self.replace_letters()
            self.is_end_game()
        

        if self.lost:

            self.terminal.print_lose_screen()
        
        else:

            self.terminal.print_win_screen()


        

    def get_input(self):

        user_input = input('Enter a letter [a-z]: ')    
        self.input = user_input


    def replace_letters(self):

        index = 0
        found_letter = False

        for letter in self.words.hidden_word:


            if self.input == letter:

                found_letter = True
                self.words.guessed_word[index] = self.input

            index += 1

        if not found_letter:

            self.stickman.lives -= 1
            self.stickman.remove_section()







    def is_end_game(self):

        if self.stickman.lives == 0: 
            
            self.inplay = False
            self.lost = True

        
        elif not "_" in self.words.guessed_word:
            
            self.inplay = False
            self.lost = False

        
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06
