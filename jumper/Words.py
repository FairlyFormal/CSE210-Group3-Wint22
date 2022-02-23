import random 



class Words():


    def __init__(self):

        self._word_list = ['bear', 'cat', 'dog', 'pig', 'cow', 'moose', 'fox'] #Simple words.
        self.random_word = Words.select_random_word(self) #Will generate a random word from word list.
    
        self.word_length = len(self.random_word) #Will use this to communicate with Terminal on how many _ there are in the log.


    def select_random_word(self):

        random_word = random.choice(self._word_list) #Selects a random word from the word list.

        return random_word #Returns said random word.


