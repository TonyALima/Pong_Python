from game import Game
from interface import *


the_window = Window()
the_window.on_init()
objects_to_render = {
    'game': {'obj': Game(),'trigger': 'Play'},
    'main_menu': {'obj': Menu(['Play', 'Options', 'About'], 50),'trigger': ''},
    'options_menu': {'obj': Menu(['Difficulty', 'Game Mode'], 64), 'trigger': 'Options'},
    'difficulty_menu': {'obj': Menu(['Hard', 'Medium', 'Easy'], 50), 'trigger': 'Difficulty'},
    'game_mode_menu': {'obj': Menu(['Multiplayer', 'Single Player'], 64), 'trigger': 'Game Mode'},
    'about_menu': {'obj': Menu(['Author: Tony Albert Lima', 'Version: 2.1', 'License: MIT', 'official repository'], 35),
        'trigger': 'About'}}

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