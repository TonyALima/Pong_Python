from game import Game
from interface import *

pygame.font.init()
objects_to_render = {
    'game': {'obj': Game(),'trigger': 'Play'},
    'main_menu': {'obj': Menu(['Play', 'Options']),'trigger': 'Esc'},
    'options_menu': {'obj': Menu(['Difficulty', 'Game Mode']), 'trigger': 'Options'}
    }

the_window = Window(objects_to_render)
for obj in objects_to_render.values():
    if isinstance(obj['obj'], Menu):
        obj['obj'].subscribe(the_window.update)
the_window.on_execute()