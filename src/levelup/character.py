import logging
from dataclasses import dataclass
from enum import Enum

#TODO: ADD THINGS YOU NEED FOR STATUS
class Character:
    #character_name: str = "Character"
    #move_count: int = 0
    #running: bool = False

    current_position: tuple = (-100, -100)

def set_character_xposition(self, xycoordinates: tuple) -> None:
    print("Set character position state for testing")
    #TODO: IMPLEMENT THIS
def getCharacterName(character_name):

    print("Get the chacater name from Controller Class")
    #TODO: IMPLEMENT THIS

def setCharacterName(character_name):
    print("Set the chacater name returned from the Controller Game Status Class")
    pass

def getPosition(x,y):
    print("Set the chacater name from Controller Class")
    pass
    

def currentPosition(x,y):
    pass

def currentPosition(x,y):
    pass

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        pass

    def create_character(self, character_name: str) -> None:
        pass

    def move(self, direction: Direction) -> None:
        pass
