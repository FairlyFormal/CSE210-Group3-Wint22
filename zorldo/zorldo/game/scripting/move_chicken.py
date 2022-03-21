from game.scripting.action import Action
from game.shared.point import Point
import random
import constants

class Chicken(Action):

    def __init__(self):
        self.times_eaten = 0
        self.last_score = ""
        self.percentage_chance_of_movement = 0

    def execute(self, cast, script):
        self._update_difficulty(cast.get_first_actor('scores'))
        foods = cast.get_actors('foods')
        for food in foods:
            if random.randint(1,100)>90-self.percentage_chance_of_movement:
                food.set_velocity(Point(random.randint(-1,1),random.randint(-1,1)).scale(constants.CELL_SIZE))
                food.move_next()
                food.set_velocity(Point(0,0))

    def _update_difficulty(self,score):
        if score != self.last_score:
            self.last_score = score
            self.times_eaten += 1
        
        self.percentage_chance_of_movement = self.times_eaten / 5