import sys
sys.path.insert(0, './src')

import pygame
import unittest
from game import Game, Scoreboard

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


class TestScoreboard(unittest.TestCase):
    test_scoreboard: Scoreboard()

    def test_mark_score(self):
        self.test_scoreboard = Scoreboard()
        
        self.test_scoreboard.mark_score(None)
        self.assertEqual(self.test_scoreboard.player_score['score'], 0)
        self.assertEqual(self.test_scoreboard.enemy_score['score'], 0)

        self.test_scoreboard.mark_score('player')
        self.assertEqual(self.test_scoreboard.player_score['score'], 1)

        self.test_scoreboard.mark_score('enemy')
        self.assertEqual(self.test_scoreboard.enemy_score['score'], 1)


if __name__ == '__main__':
    unittest.main()