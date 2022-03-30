import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()

    def get_head(self):
        return self._segments[0]

    def move_zorldo(self):

        x = (self._position.get_x() + self._velocity.get_x()) % 600
        y = (self._position.get_y() + self._velocity.get_y()) % 900
        self._segments = Point(x, y)
        return self.position

    def grow_tail(self, number_of_segments):
        return

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        position = Point(x - 1 * constants.CELL_SIZE, y)
        velocity = Point(1, 0)
        text = "('_')"
        color = constants.YELLOW if 1 == 0 else constants.GREEN
            
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)