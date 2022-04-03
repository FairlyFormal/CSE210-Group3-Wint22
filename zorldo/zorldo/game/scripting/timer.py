import time
import datetime
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class Timer():

    def __init__(self):
        self._now = datetime.datetime.now()
        self._later = datetime.datetime.now()
        self._diff_delta = self._later - self._now
        self._seconds = 0
        self._is_game_over = False


    def execute(self,cast,script):


        if not self._is_game_over:
            # self._tell_them_to_get_chickens(cast)
            self._count_up()
            if self._seconds > 30:
                        self._is_game_over = True
            self._handle_game_over(cast)


    def _count_up(self):
        self._later = datetime.datetime.now()
        self._diff_delta = self._later - self._now
        if self._seconds != self._diff_delta.total_seconds():
            self._seconds = self._diff_delta.total_seconds()

    def _tell_them_to_get_chickens(self,cast):
        if self._seconds == 0 and len(cast.get_actors('start_messages')) == 0:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Get as many chickens as you can in 30 seconds!")
            message.set_position(position)
            cast.add_actor("start_messages", message)
        
        if self._seconds > 5 and len(cast.get_actors('start_messages')) != 0:
            cast.remove_actor("start_messages", message)
            pass


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_actors("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for chicken in food:
                chicken.set_color(constants.WHITE)
                chicken._points = 0


