import sys
sys.path.insert(0, './src')

import pygame
import unittest
from game import Game

class TestGame(unittest.TestCase):
    test_game: Game

    def test_check_collision(self):
        self.test_game = Game()
        pygame.init()
        # first move
        self.test_game.entities_dict['ball'].loop()

        # don't colliding
        self.test_game.check_collision()
        self.assertFalse(self.test_game.entities_dict['ball'].is_colliding)

        # enemy position
        self.test_game.entities_dict['ball'].rect.top = 34 

        # colliding with enemy
        self.test_game.check_collision()
        self.assertTrue(self.test_game.entities_dict['ball'].is_colliding)

        pygame.quit()


    def test_check_goal(self):
        self.test_game = Game()
        pygame.init()

        # pleyer goal
        self.test_game.entities_dict['ball'].rect.top = 0
        self.assertTrue(self.test_game.check_goal())

        #enemy goal
        self.test_game.entities_dict['ball'].rect.bottom = 400
        self.assertTrue(self.test_game.check_goal())
        pygame.quit()


if __name__ == '__main__':
    unittest.main()