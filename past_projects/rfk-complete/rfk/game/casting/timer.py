from game.casting.actor import Actor
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
import time


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "The Chicken Chaser"
DEFAULT_ARTIFACTS = 40

        
class Timer(Actor):

    def __init__(self):

        self.count = 59
        super().__init__()
        self.countdown(59)


    def countdown(self, t):

        keyboard_service = KeyboardService(CELL_SIZE)
        video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
        
        while Director(keyboard_service, video_service)._video_service.is_window_open():

            mins, secs = divmod(t, 60)
            timer = '{:02d}'.format(secs)
            self.set_text(timer)
            time.sleep(1)
            t -= 1
    