from game import Game
from interface import *


the_window = Window()
the_window.on_init()
objects_to_render = {
    'game': {'obj': Game(),'trigger': 'Play'},
    'main_menu': {'obj': Menu(['Play', 'Options']),'trigger': ''},
    'options_menu': {'obj': Menu(['Difficulty', 'Game Mode']), 'trigger': 'Options'},
    'difficulty_menu': {'obj': Menu(['Hard', 'Medium', 'Easy']), 'trigger': 'Difficulty'},
    'game_mode_menu': {'obj': Menu(['Multiplayer', 'Single Player']), 'trigger': 'Game Mode'}
    }

main_menu_triggers = 'Esc Hard Medium Easy Multiplayer Single Player'

objects_to_render['main_menu']['trigger'] = main_menu_triggers

the_window.subscribe_to_render(objects_to_render)

the_window.update('Esc')

for obj in objects_to_render.values():
    if isinstance(obj['obj'], (Game, Menu)):
        obj['obj'].subscribe(the_window.update)
    if obj['trigger'] in 'Difficulty Game Mode':
        obj['obj'].subscribe(objects_to_render['game']['obj'].update)

the_window.on_execute()