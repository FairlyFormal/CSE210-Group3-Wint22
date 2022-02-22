from Words import Words
import Stickman
import Commander

class Terminal():
    
    def __init__(self):

        pass


    def print_guessed_word(self, guessed_word):

        for letter in guessed_word:

            print(letter, end = " ")
        
        print()


    def print_win_screen(self):


        print('\n================ YOU WON ===================\n')


    def print_lose_screen(self):

        print('\n================ YOU LOST ===================\n')
