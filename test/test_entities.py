import sys
from unittest.case import expectedFailure
sys.path.insert(0, './src')

import pygame
import unittest
from entities import *
from random import randint


class TestPlayer(unittest.TestCase):
    def test_move(self):
        test_player = Player()

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
    def test_cacl_angle(self):
        test_ball = Ball()
        test_ball.direction_up = True
        test_angle = test_ball.calc_angle()
        self.assertIn(test_angle, range(30, 151))

        test_ball.direction_up = False
        test_angle = test_ball.calc_angle()
        self.assertIn(test_angle, range(210, 331))

    def test_calc_movement(self):
        test_ball = Ball()
        test_ball.calc_movement(randint(0, 90))

        self.assertTrue(0 < test_ball.dx < 1)
        self.assertTrue(0 < test_ball.dy < 1)


class TestEnemy(unittest.TestCase):
    def test_npc_move(self):
        test_ball = Ball()
        test_enemy = Enemy(test_ball)
        test_ball.loop()
        test_enemy.loop()
        expected_position = test_ball.rect.centerx * test_enemy.accuracy
        self.assertEqual(test_enemy.rect.centerx, expected_position)


if __name__ == '__main__':
    pygame.init()
    unittest.main()
    pygame.quit()

