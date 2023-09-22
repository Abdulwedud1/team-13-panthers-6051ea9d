import pyfiglet
from enum import Enum

class Font(Enum):
    BIG = "larry3d"
    SMALL = "threepoint"

class Logo:

    def render(self, T: str, font: Font ) -> str:
        
        ASCII_art= pyfiglet.figlet_format(T, font.value)
        return ASCII_art


