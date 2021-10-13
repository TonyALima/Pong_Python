import pygame
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
            if isinstance(self.obj_on_screen, (Game)):
                self.obj_on_screen.on_loop()
                self.obj_on_screen.on_render(self._display_surf)

            # Control and show FPS
            self.FPS.tick(60)
            print(f'FPS: {self.FPS.get_fps()}')

            pygame.display.update()

        self.on_cleanup()

