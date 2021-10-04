from pygame.locals import *
import pygame.draw
import pygame.rect
from random import getrandbits, randint
from math import radians, cos, sin


class Entity(pygame.sprite.Sprite):
    def __init__(self, rect: pygame.rect.Rect, color, initial_position: tuple):
        super().__init__()
        self.rect = rect
        self. color = color
        self.initial_position = initial_position
        self.rect.center = initial_position

    def loop(self):
        pass

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def restart(self):
        self.rect.center = self.initial_position


class Player(Entity):
    def __init__(self):
        super().__init__(pygame.rect.Rect(0, 0, 200, 20), (0, 255, 0), (320, 375))

    def loop(self):
        self.move()

    def move(self, right=False, left=False):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_RIGHT] or right:
            if self.rect.right < 640:
                self.rect.move_ip(5, 0)

        if pressed_keys[K_LEFT] or left:
            if self.rect.left > 0:
                self.rect.move_ip(-5, 0)


class Ball(Entity):
    def __init__(self, speed):
        super().__init__(pygame.rect.Rect(0, 0, 16, 16), (200, 200, 0), (320, 200))
        self.speed = speed
        self.direction_up = bool(getrandbits(1)) # random boolean
        self.is_colliding = True
        self.dx: float
        self.dy: float

    def loop(self):
        if self.is_colliding:
            self.calc_movement(self.calc_angle())
            self.is_colliding = False
        
        if self.rect.right >= 640 or self.rect.left <= 0:
            self.dx *= -1
        self.rect.move_ip(self.dx * self.speed,
                            self.dy * self.speed)

    def calc_angle(self):
        if self.direction_up:
            angle = randint(30, 150)
        else:
            angle = randint(210, 330)
        self.direction_up = not self.direction_up

        return angle

    def calc_movement(self, angle):
        self.dx = cos(radians(angle))
        self.dy = sin(radians(angle))


class Enemy(Entity):
    def __init__(self, precision, ball: Ball):
        super().__init__(pygame.rect.Rect(0, 0, 200, 20), (255, 0, 0), (320, 25))
        self.precision = precision
        self.ball = ball

    def loop(self):
        self.rect.move_ip(self.follow_ball(), 0)

    def follow_ball(self):
        return (self.ball.rect.centerx - self.rect.centerx) * self.precision

