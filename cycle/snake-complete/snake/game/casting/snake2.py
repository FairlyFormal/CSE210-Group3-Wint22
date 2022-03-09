from game.casting.snake import Snake
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Snake2(Snake):

    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def _prepare_body(self):
        x = int(300)
        y = int(300)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.RED if i == 0 else constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)