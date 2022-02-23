class Stickman():


    def __init__(self):
        
        self.stickman = ['  ___  ',' /___\ ',' \   / ','  \ /  ','   0   ','  /|\  ','  / \   '] 
        self.lives = 7



    def draw_stickman(self): #Draws the entire stickman. It will be updated through the game

        stickman = self.stickman

        for line in stickman:

            print(line)

    

    def remove_section(self): #Removes a section and subtracts a life.

        self.stickman.pop(0)