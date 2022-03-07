import random 



class Words():


    def __init__(self):

<<<<<<< HEAD
        self._word_list = ['bear', 'cat', 'dog', 'pig', 'cow', 'moose', 'fox'] #Simple words.
        self.random_word = Words.select_random_word(self) #Will generate a random word from word list.
    
        self.word_length = len(self.random_word) #Will use this to communicate with Terminal on how many _ there are in the log.
=======
        self._word_list = ['bear', 'cat', 'dog', 'pig', 'cow', 'moose', 'fox']
        self.hidden_word = self.select_random_word()
        self.guessed_word = self.initialize_guessed_word()

>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06


    def select_random_word(self):

<<<<<<< HEAD
        random_word = random.choice(self._word_list) #Selects a random word from the word list.
=======
        random_word = random.choice(self._word_list) 
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06

        return random_word #Returns said random word.


<<<<<<< HEAD
=======
    def initialize_guessed_word(self): 

        guessed_word = []

        for i in self.hidden_word: 

            guessed_word.append("_") 
   
        return guessed_word

>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06
