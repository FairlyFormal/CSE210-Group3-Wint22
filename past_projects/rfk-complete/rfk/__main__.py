import os
import random
import time

from game.casting.actor import Actor
from game.casting.timer import Timer
from game.casting.score import Score
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "The Chicken Chaser"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the scoreboard
    score_message = Score()
    score_message.set_text('Score: ' + str(score_message.points))
    score_message.set_font_size(30)
    score_message.set_color(WHITE)
    score_message.set_position(Point(25, 25))
    cast.add_actor("score", score_message)


    # create the timer

    game_timer = Timer()
    game_timer.set_font_size(50)
    game_timer.set_color(WHITE)
    game_timer.set_position(Point(100, 100))
    cast.add_actor("score", game_timer)



    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)



    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()

    # for n in range(DEFAULT_ARTIFACTS):
    #     text = chr(random.randint(33, 126))
    #     message = messages[n]

    #     x = random.randint(1, COLS - 1)
    #     y = random.randint(1, ROWS - 1)
    #     position = Point(x, y)
    #     position = position.scale(CELL_SIZE)

    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = Color(r, g, b)
        
    #     artifact = Artifact()
    #     artifact.set_text(text)
    #     artifact.set_font_size(FONT_SIZE)
    #     artifact.set_color(color)
    #     artifact.set_position(position)
    #     artifact.set_message(message)
    #     cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()