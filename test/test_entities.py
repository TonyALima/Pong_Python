import sys
sys.path.insert(0, './src')

import pygame
import unittest
import entities
from random import randint


pygame.init()

class TestPlayer(unittest.TestCase):
    def test_move(self):
        test_player = entities.Player()

        expected_position = test_player.rect.centerx
        test_player.move()
        self.assertEqual(test_player.rect.centerx, expected_position)

        expected_position -= 5
        test_player.move(left=True)
        self.assertEqual(test_player.rect.centerx, expected_position)

        expected_position += 5
        test_player.move(right=True)
        self.assertEqual(test_player.rect.centerx, expected_position)


class TestBall(unittest.TestCase):
    test_ball: entities.Ball

    def test_cacl_angle(self):
        self.test_ball = entities.Ball(speed=1)
        self.test_ball.direction_up = True
        test_angle = self.test_ball.calc_angle()
        self.assertIn(test_angle, range(30, 151))

        self.test_ball.direction_up = False
        test_angle = self.test_ball.calc_angle()
        self.assertIn(test_angle, range(210, 331))

    def test_calc_movement(self):
        self.test_ball = entities.Ball(speed=1)
        self.test_ball.calc_movement(randint(0, 90))

        self.assertTrue(0 < self.test_ball.dx < 1)
        self.assertTrue(0 < self.test_ball.dy < 1)


class TestEnemy(unittest.TestCase):
    test_enemy: entities.Enemy
    
    def test_follow_ball(self):
        test_ball = entities.Ball(speed=1)
        self.test_enemy = entities.Enemy(accuracy=1, ball=test_ball)
        test_ball.loop()
        next_position = self.test_enemy.rect.centerx + self.test_enemy.move()

        self.assertEqual(test_ball.rect.centerx, next_position)


if __name__ == '__main__':
    unittest.main()

