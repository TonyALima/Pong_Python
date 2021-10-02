from _typeshed import Self
from abc import abstractclassmethod
from pygame.constants import K_LEFT, K_RIGHT
import pygame.draw
import pygame.rect


class Entity(pygame.sprite.Sprite):
    def __init__(self, rect: pygame.rect.Rect, color):
        super.__init__()
        self.rect = rect
        self. color = color

    def loop(self):
        pass

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Player(Entity):
    def __init__(self):
        super().__init__(pygame.rect.Rect(220, 300, 200, 50), (0, 255, 0))

    @abstractclassmethod
    def loop(self):
        self.move()

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            if self.rect.right < 640:
                self.rect.move_ip(5, 0)

        if pressed_keys[K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-5, 0)



class Enemy(Entity):
    def __init__(self):
        super().__init__(pygame.rect.Rect(220, 50, 200, 50), (255, 0, 0))