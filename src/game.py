import pygame
import pygame.time
import pygame.draw
import pygame.font
import pygame.surface
from entities import *


class Game:

    def __init__(self):
        self.entities_dict = {'player': Player(),'ball': Ball(5)}
        self.entities_dict['enemy'] = Enemy(1, self.entities_dict['ball'])
        self.collide_rects = []
        for key, value in self.entities_dict.items():
            if key != 'ball':
                self.collide_rects.append(value.rect)
        self.scoreboard = Scoreboard()
        self.accepted_moves = self.create_moves()
        self.observers = []

    def create_moves(self):
        def k_right():
            self.entities_dict['player'].move(right=True)

        def k_left():
            self.entities_dict['player'].move(left=True)

        def k_esc():
            self.notify_all('Esc')

        return {
            K_RIGHT: k_right,
            K_LEFT: k_left,
            K_ESCAPE: k_esc
        }

    def subscribe(self, observer_function):
        self.observers.append(observer_function)

    def notify_all(self, command):
        print('notifying')
        for observer_function in self.observers:
            observer_function(command)

    def check_collision(self):
        collided_index = self.entities_dict[
            'ball'].rect.collidelist(self.collide_rects)
        
        if collided_index != -1:
            self.entities_dict['ball'].is_colliding = True

    def check_goal(self):
        if self.entities_dict['ball'].rect.top <= 0:
            return 'player'

        elif self.entities_dict['ball'].rect.bottom >= 400: 
            return 'enemy'

        else:
            return None

    def on_loop(self):
        self.check_collision()
        who_scored = self.check_goal()
        if who_scored:
            for entity in self.entities_dict.values():
                entity.restart()
            
            self.scoreboard.mark_score(who_scored)

        for entity in self.entities_dict.values():
            entity.loop()

    def on_render(self, surface):
        surface.fill((3, 61, 18, 24))
        for entity in self.entities_dict.values():
            entity.render(surface)
        self.scoreboard.render(surface)


class Scoreboard():
    def __init__(self):
        self.player_score = {'rect': pygame.Rect(620, 186, 20, 28), 
                                'score': 0}
        self.enemy_score = {'rect': pygame.Rect(0, 186, 20, 28), 
                                'score': 0}
        self.rects_color = (8, 152, 196, 77)
        self.font = pygame.font.SysFont('arial', 22)

    def render(self, surface):
        self.draw_score(surface, self.player_score)
        self.draw_score(surface, self.enemy_score)
        

    def draw_score(self, surface, entity):
        pygame.draw.rect(surface, self.rects_color, entity['rect'])
        textsurface = self.font.render(f"{entity['score']}", False, (255, 255, 255))
        surface.blit(textsurface, (entity['rect'].left + 5, 191))

    def mark_score(self, who):
        if who == 'player':
            self.player_score['score'] += 1
        if who == 'enemy':
            self.enemy_score['score'] += 1
