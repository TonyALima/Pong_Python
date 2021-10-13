from game import Game
from interface import *

pygame.font.init()
objects_to_render = {'menu': MainMenu(),
                    'game': Game()}

the_window = Window(objects_to_render)
objects_to_render['menu'].observers.append(the_window.update)
the_window.on_execute()