import pygame
import pygame.time
import pygame.draw
from entities import *


class Game:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.FPS = pygame.time.Clock()
        self.entities_dict = {'player': Player(),'ball': Ball(5)}
        self.entities_dict['enemy'] = Enemy(1, self.entities_dict['ball'])
        self.collide_rects = []
        for key, value in self.entities_dict.items():
            if key != 'ball':
                self.collide_rects.append(value.rect)

    def check_collision(self):
        collided_index = self.entities_dict[
            'ball'].rect.collidelist(self.collide_rects)
        
        if collided_index != -1:
            self.entities_dict['ball'].is_colliding = True

    def check_goal(self):
        return self.entities_dict['ball'].rect.top <= 0 or \
            self.entities_dict['ball'].rect.bottom >= 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        pygame.display.set_caption("Pong_Python")

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.check_collision()
        if self.check_goal():
            for entity in self.entities_dict.values():
                entity.restart()
            
            ## Todo: Mark the scoreboard

        for entity in self.entities_dict.values():
            entity.loop()

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        for entity in self.entities_dict.values():
            entity.render(self._display_surf)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            
            # Game loop
            self.on_loop()
            self.on_render()

            # Control and show FPS
            self.FPS.tick(60)
            print(f'FPS: {self.FPS.get_fps()}')

            pygame.display.update()

        self.on_cleanup()

if __name__ == "__main__" :
    theGame = Game()
    theGame.on_execute()