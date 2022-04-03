from game.shared.color import Color
import pathlib

ROOT_PATH = pathlib.Path(__file__).parent.resolve().parent.resolve()

COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 1200
MAX_Y = 900
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Zorldo: Chicken Chaser"
SNAKE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

CHICKEN_SOUND = str(ROOT_PATH.joinpath("zorldo/game/sounds/chicken.wav"))