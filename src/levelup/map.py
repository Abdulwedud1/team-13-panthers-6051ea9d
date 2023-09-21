from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    starting_position = Position(0,0)
    positions = []
    size: Tuple[int, int] = (10, 10)

    def __init__(self):
        pass

    def create_positions(self) -> None:
        pass

    def is_position_valid(self, position :Position):
        pass

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
      pass
        
        