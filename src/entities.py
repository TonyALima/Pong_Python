import pygame.draw
import pygame.rect
from random import getrandbits, randint
from math import radians, cos, sin


class Entity(pygame.sprite.Sprite):
    def __init__(self, rect: pygame.rect.Rect, color, initial_position: tuple):
        super().__init__()
        self.rect = rect
        self.color = color
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

    def move(self, right=False, left=False):

        if right:
            if self.rect.right < 640:
                self.rect.move_ip(5, 0)

        if left:
            if self.rect.left > 0:
                self.rect.move_ip(-5, 0)


class Ball(Entity):
    def __init__(self):
        super().__init__(pygame.rect.Rect(0, 0, 16, 16), (200, 200, 0), (320, 200))
        self.direction_up = bool(getrandbits(1)) # random boolean
        self.is_colliding = False
        self.dx: float
        self.dy: float
        self.x_cooldown = 0
        self.y_cooldown = 0
        self.speed = 0
        self.calc_movement(self.calc_angle())

    def loop(self):
        if self.is_colliding and self.y_cooldown <= 0:
            self.move_at_colliding()
        
        if self.is_bouncing() and self.x_cooldown <= 0:
            self.bounce()

        self.rect.move_ip(self.dx * self.speed,
                            self.dy * self.speed)

        self.cooldown()

    def move_at_colliding(self):
        self.calc_movement(self.calc_angle())
        self.y_cooldown = 30

    def cooldown(self):
        self.x_cooldown -= 1
        self.y_cooldown -= 1
        self.is_colliding = False

    def bounce(self):
        self.dx *= -1
        self.x_cooldown = 3

    def is_bouncing(self):
        return self.rect.right >= 640 or self.rect.left <= 0

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

    def restart(self):
        super().restart()
        self.calc_movement(self.calc_angle())


class Enemy(Entity):
    def __init__(self, ball: Ball):
        super().__init__(pygame.rect.Rect(0, 0, 200, 20), (255, 0, 0), (320, 25))
        self.accuracy = 1
        self.ball = ball
        self.is_npc = True

    def loop(self):
        self.move()

    def move(self, right=False, left=False):
        if self.is_npc:
            movement = (self.ball.rect.centerx - self.rect.centerx) * self.accuracy
            self.rect.move_ip(movement, 0)
        else:
            if right:
                if self.rect.right < 640:
                    self.rect.move_ip(5, 0)

            if left:
                if self.rect.left > 0:
                    self.rect.move_ip(-5, 0)
