from game import Game
from interface import *

the_game = Game()
menu = MainMenu()

the_window = Window(menu)
the_window.on_execute()