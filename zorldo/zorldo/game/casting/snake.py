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

        self.y = 500
        self.x = 500

        super().__init__()
        self._segments = []
        self._prepare_body()


    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            
            segment.move_next()
        # update velocities

    def get_head(self):

        return self._segments[0]

    def grow_tail(self, number_of_segments):
        return

        # for i in range(number_of_segments):
        #     tail = self._segments[-1]
        #     velocity = tail.get_velocity()
        #     offset = velocity.reverse()
        #     position = tail.get_position().add(offset)
            
        #     segment = Actor()
        #     segment.set_position(position)
        #     segment.set_velocity(velocity)
        #     segment.set_text("#")
        #     segment.set_color(constants.GREEN)
        #     self._segments.append(segment)

    def turn_head(self, velocity):

        self._segments[0].set_velocity(velocity)

    
    def _prepare_body(self):

        x = self.x
        y = self.y

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = 0
            text = "('_')"
            color = constants.YELLOW if i == 0 else constants.GREEN
            

            segment = Actor()
            segment.set_position(position)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)