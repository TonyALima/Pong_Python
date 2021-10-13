from game import Game
from interface import *

pygame.font.init()
objects_to_render = {
    'main_menu': {'obj': Menu(['Play', 'Options']),'trigger': ''},
    'game': {'obj': Game(),'trigger': 'Play'},
    'options': {'obj': Menu(['Difficulty', 'Game Mode']), 'trigger': 'Options'}
    }

the_window = Window(objects_to_render)
objects_to_render['main_menu']['obj'].observers.append(the_window.update)
the_window.on_execute()