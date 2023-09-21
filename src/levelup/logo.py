
import pyfiglet

class Logo:

    T = "Welcome            to      Achipelago"

    def render(self):

        ASCII_art = pyfiglet.figlet_format(self.T, font = "larry3d")
        print((ASCII_art))

        self.T = "     by Team 13 - Panther"
        ASCII_art_1 = pyfiglet.figlet_format(self.T, font = "threepoint")
        print(ASCII_art_1)


