import random

class Player:
    

    def __init__(self):

        self.score = 300

    def show_score(self):

        print(self.score)
    
    def check_score(self):

        if self.score <= 0:
            print('Game Over. Thanks for playing.\n')
            quit()
        else:
            pass

class Game:


    def __init__(self, card_1=0, card_2=0):

        self.in_play = True
        self.random_card = random.randint(1, 13)
        self.card_1 = 0
        self.card_2 = 0


    def continue_game(self):

        continue_game = input('Keep playing? (y/n): ')

        if (continue_game == 'y') or (continue_game == 'Y'):

            new_game.continue_game_logic()

        elif (continue_game == 'n') or (continue_game == 'N'):

            print('Thanks for playing. :-)\n')
            return

        else:

            print('Thanks for playing.\n')
            return

    


    def start_game(self):

        # Asks for user input and generates relevant variables...

        print('\nWelcome to the game.')

        self.card_1 = random.randint(1, 13)

        print(f'The Card is {self.card_1}')

        guess = input('Higher or lower? (h/l): ')

        self.card_2 = random.randint(1, 13)

        print(f'Next card was: {self.card_2}')


        #Once variables are set into place then there is an if statement to evaluate decisions and integers.

        if (guess == 'h' or guess == 'H') and (self.card_1 < self.card_2):

            new_player.score += 100

        elif (guess == 'l' or guess == 'L') and (self.card_1 > self.card_2):

            new_player.score += 100

        else:

            new_player.score -= 75
            new_player.check_score()

        self.card_1 = self.card_2



        #Tells the player their score and asks to continue game.

        print('Your score is: ' + str(new_player.score))
        new_game.continue_game()
        
    def continue_game_logic(self):

        # Asks for user input and generates relevant variables...

        print(f'\nThe Card is {self.card_1}')

        guess = input('Higher or lower? (h/l): ')

        self.card_2 = random.randint(1, 13)

        print(f'Next card was: {self.card_2}')


        #Once variables are set into place then there is an if statement to evaluate decisions and integers.

        if (guess == 'h' or guess == 'H') and (self.card_1 < self.card_2):

            new_player.score += 100

        elif (guess == 'l' or guess == 'L') and (self.card_1 > self.card_2):

            new_player.score += 100

        else:

            new_player.score -= 75
            new_player.check_score()

        self.card_1 = self.card_2



        #Tells the player their score and asks to continue game.

        print('Your score is: ' + str(new_player.score))
        new_game.continue_game()



# Creating the objects for the game (player and game).

new_player = Player()
new_game = Game()


#The game played out.


new_game.start_game()
