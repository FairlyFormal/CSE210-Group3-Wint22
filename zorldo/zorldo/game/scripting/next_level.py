import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService

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
        self._level = 1
        self._playing = False

    def execute(self,cast,script):
        if self._playing:
            print("Hunter is debugging.")
            pass
        else:
            pass
            # print("Zorldo: Chicken Chaser")
            # print("")

        pass