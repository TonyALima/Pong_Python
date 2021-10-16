import pygame
import pygame.font
import pygame.draw
from math import floor
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_ESCAPE
from game import Game


class Window():

    def __init__(self, objects_to_render: dict):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.FPS = pygame.time.Clock()
        self.objects_to_render = objects_to_render
        self.object_in_render = objects_to_render['main_menu']['obj']
        self.is_key_pressed = False

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
                    self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        pygame.display.set_caption("Pong_Python")

    def on_cleanup(self):
        pygame.quit()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def update(self, trigger):
        for obj in self.objects_to_render.values():
            if obj['trigger'] == trigger:
                self.object_in_render = obj['obj']
                break

    def keyboard_listener(self):
        in_game = isinstance(self.object_in_render, Game)
        key_released = True
        pressed_keys = pygame.key.get_pressed()
        for key in self.object_in_render.accepted_moves.keys():
            if pressed_keys[key]:
                key_released = False
                if in_game or not self.is_key_pressed:
                    self.object_in_render.accepted_moves[key]()
        self.is_key_pressed = not key_released

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            
            # Main loop
            if isinstance(self.object_in_render, (Game, Menu)):
                self.keyboard_listener()
                self.object_in_render.on_loop()
                self.object_in_render.on_render(self._display_surf)

            # Control and show FPS
            self.FPS.tick(60)
            print(f'FPS: {self.FPS.get_fps()}')

            pygame.display.update()

        self.on_cleanup()


class Menu():
    
    def __init__(self, buttons_text):
        self.font = pygame.font.SysFont('arial', 64)
        size_button = self.calc_size_button(len(buttons_text))
        self.buttons = [self.create_button(text, index, size_button)
                        for index, text in enumerate(buttons_text)]

        self.high_light =self.create_high_light(size_button)
        self.observers = []
        self.accepted_moves = self.create_moves()

    def create_moves(self):
        def k_up():
            if self.high_light['position'] > 0:
                self.high_light['position'] -= 1

        def k_down():
            if self.high_light['position'] < len(self.buttons) - 1:
                self.high_light['position'] += 1

        def k_enter():
            selected_button = self.buttons[self.high_light['position']]['text']
            self.notify_all(selected_button)

        def k_esc():
            self.notify_all('Esc')

        return {
            K_UP: k_up,
            K_DOWN: k_down,
            K_RETURN: k_enter,
            K_ESCAPE: k_esc
        }

    def notify_all(self, command):
        print('notifying')
        for observer_function in self.observers:
            observer_function(command)

    def subscribe(self, observer_function):
        self.observers.append(observer_function)

    def update_high_light(self):
        active_button_center = self.buttons[self.high_light['position']]['rect'].center
        self.high_light['rect'].center = active_button_center

    def on_loop(self):
        self.update_high_light()

    def on_render(self, surface):
        surface.fill((25, 83, 72))
        
        pygame.draw.rect(surface, self.high_light['color'],
                            self.high_light['rect'])
        
        for button in self.buttons:
            self.draw_button(surface, button)

    def create_button(self, text, position, size):
        height, spacing, top_space = size
        width = 4 * height
        rect_top = 75 + top_space + (position * (height + spacing))
        rect_left = (640 - width) / 2
        rect = pygame.Rect(rect_left, rect_top, width, height)
        text_color = (200, 200, 200)
        back_color = (50, 50, 50)
        text_surface = self.font.render(text, False, text_color)

        return {'text_surface': text_surface,
                'text': text,
                'rect': rect,
                'color': back_color}

    def create_high_light(self, size):
        height = size[0] + 10
        width = 4 * size[0] +10
        return {'position': 0,
                'rect': pygame.Rect(0, 0, width, height),
                'color': (200, 200, 200)}

    def calc_size_button(self, amount):
        height = floor((250/amount)*0.8)
        spacing = floor((250-height*amount)/(amount -1))
        rest_top = floor((250-height*amount) - (spacing *(amount-1)))
        return height, spacing, rest_top

    def draw_button(self, suface: pygame.Surface, button):
        pygame.draw.rect(suface, button['color'], button['rect'])

        text_width, text_height = self.font.size(button['text'])
        text_left = button['rect'].left + (button['rect'].width - text_width) / 2
        text_top = button['rect'].top + (button['rect'].height - text_height) / 2

        suface.blit(button['text_surface'], (text_left, text_top))