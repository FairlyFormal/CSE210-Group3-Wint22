import random 



class Words():


    def __init__(self):

        self._word_list = ['bear', 'cat', 'dog', 'pig', 'cow', 'moose', 'fox']
        self.hidden_word = self.select_random_word()
        self.guessed_word = self.initialize_guessed_word()



    def select_random_word(self):

        random_word = random.choice(self._word_list) 

        return random_word #Returns said random word.


    def initialize_guessed_word(self): 

        guessed_word = []

        for i in self.hidden_word: 

            guessed_word.append("_") 
   
        return guessed_word

