import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class NextLevel(Action):
    """ This class initializes each level. 
    It:

    checks if the chickens are gone or if timer ran out
    game over if timer ran out

    next level if chickens are gone
        spawns chickens based on level number
        resets the timer to one minute
        starts the level when the user hits enter

    Use it to start the game, move between levels, and do game over."""

    def __init__(self):
        pass