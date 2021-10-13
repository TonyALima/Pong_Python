import pygame
import pygame.font
import pygame.draw
from pygame.locals import K_UP, K_DOWN
from game import Game


class Window():

    def __init__(self, obj_on_screen = None):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.FPS = pygame.time.Clock()
        self.obj_on_screen = obj_on_screen

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

    def update():
        pass

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            
            # Main loop
            if isinstance(self.obj_on_screen, (Game, MainMenu)):
                self.obj_on_screen.on_loop()
                self.obj_on_screen.on_render(self._display_surf)

            # Control and show FPS
            self.FPS.tick(60)
            print(f'FPS: {self.FPS.get_fps()}')

            pygame.display.update()

        self.on_cleanup()


class MainMenu():
    
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 64)
        buttons_text = ['Play', 'Options']
        self.buttons = [self.create_button(text, index)
                        for index, text in enumerate(buttons_text)]

        self.high_light = {'position': 0,
                            'rect': pygame.Rect(0, 0, 410, 110),
                            'color': (200, 200, 200)}

    def update_high_light(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP] and self.high_light['position'] > 0:
            self.high_light['position'] -= 1

        if pressed_keys[K_DOWN] and self.high_light['position'] < len(self.buttons) - 1:
            self.high_light['position'] += 1

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

    def create_button(self, text, position):
        rect_top = 75 + (position * 150)
        rect = pygame.Rect(120, rect_top, 400, 100)
        text_color = (200, 200, 200)
        back_color = (50, 50, 50)
        text_surface = self.font.render(text, False, text_color)

        return {'text_surface': text_surface,
                'text': text,
                'rect': rect,
                'color': back_color}

    def draw_button(self, suface: pygame.Surface, button):
        pygame.draw.rect(suface, button['color'], button['rect'])

        text_width, text_height = self.font.size(button['text'])
        text_left = button['rect'].left + (button['rect'].width - text_width) / 2
        text_top = button['rect'].top + (button['rect'].height - text_height) / 2

        suface.blit(button['text_surface'], (text_left, text_top))