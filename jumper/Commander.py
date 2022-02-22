import Words
import Terminal_Butler
import Stickman




class Commander():


    def __init__(self):

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

        