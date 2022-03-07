class Stickman():


<<<<<<< HEAD
    #There is 3 parts to this class:

    #The first part contains a list with the stickman parts (What Hunter did yesterday in class).

    #The second part is drawing the stickman, it will print (line by line) every character in the list. This draws the picture of the stickman.

    #The third part is removing a section of the stickman, removing a life.


    def __init__(self):
        
        self.stickman = [""] #Put the stickman parts within the list here. HUNTER KNOWS HOW TO DO THIS. I COULDN'T FIND THE PARTS.
        self.lives = 0 #The amount of stickman parts is the same as the number of lives the stickman has. 0 is just a placeholder.
=======
    def __init__(self):
        
        self.stickman = ['  ___  ',' /___\ ',' \   / ','  \ /  ','   0   ','  /|\  ','  / \   '] 
        self.lives = 7
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06



    def draw_stickman(self): #Draws the entire stickman. It will be updated through the game

        stickman = self.stickman

        for line in stickman:
<<<<<<< HEAD
            
            print(f"\n {stickman}")
=======

            print(line)
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06

    

    def remove_section(self): #Removes a section and subtracts a life.

<<<<<<< HEAD
        self.stickman.pop(0) #Removes the first element in the stickman list (This may be backwars, should probably check.)

        return self.stickman() #Returns the updated Stickman.
=======
        self.stickman.pop(0)
>>>>>>> ec0fa9d2461e564d333dcb45c9f5e0c0086d2d06
