import sys
sys.path.insert(0, './src')

import pygame
import unittest
from game import Game, Scoreboard
from pygame.locals import K_RIGHT, K_LEFT, K_ESCAPE
from pygame.locals import K_a as K_A
from pygame.locals import K_d as K_D

class TestGame(unittest.TestCase):

    def test_moves(self):
        pygame.font.init()

        test_game = Game()
        moves = test_game.create_moves()
        moves[K_RIGHT]()
        expected_value = test_game.entities_dict['player'].initial_position[0] + 5
        value = test_game.entities_dict['player'].rect.centerx
        self.assertEqual(value, expected_value)

        test_game = Game()
        moves = test_game.create_moves()
        moves[K_LEFT]()
        expected_value = test_game.entities_dict['player'].initial_position[0] - 5
        value = test_game.entities_dict['player'].rect.centerx
        self.assertEqual(value, expected_value)

        test_game = Game()
        moves = test_game.create_moves()
        test_game.entities_dict['enemy'].is_npc = False
        moves[K_D]()
        expected_value = test_game.entities_dict['enemy'].initial_position[0] + 5
        value = test_game.entities_dict['enemy'].rect.centerx
        self.assertEqual(value, expected_value)

        test_game = Game()
        moves = test_game.create_moves()
        test_game.entities_dict['enemy'].is_npc = False
        moves[K_A]()
        expected_value = test_game.entities_dict['enemy'].initial_position[0] - 5
        value = test_game.entities_dict['enemy'].rect.centerx
        self.assertEqual(value, expected_value)

        pygame.font.quit()

    def test_update_difficulty(self):
        pygame.font.init()
        test_game = Game()

        test_game.update_difficulty('Hard')
        expected_value = 9
        value = test_game.entities_dict['ball'].speed
        self.assertEqual(value, expected_value)
        expected_value = 0.06
        value = test_game.entities_dict['enemy'].accuracy
        self.assertEqual(value, expected_value)

        test_game.update_difficulty('Medium')
        expected_value = 6.5
        value = test_game.entities_dict['ball'].speed
        self.assertEqual(value, expected_value)
        expected_value = 0.038
        value = test_game.entities_dict['enemy'].accuracy
        self.assertEqual(value, expected_value)

        test_game.update_difficulty('Easy')
        expected_value = 5
        value = test_game.entities_dict['ball'].speed
        self.assertEqual(value, expected_value)
        expected_value = 0.02
        value = test_game.entities_dict['enemy'].accuracy
        self.assertEqual(value, expected_value)

        test_game.update_difficulty('induced error')
        expected_value = 5
        value = test_game.entities_dict['ball'].speed
        self.assertEqual(value, expected_value)
        expected_value = 0.02
        value = test_game.entities_dict['enemy'].accuracy
        self.assertEqual(value, expected_value)

        pygame.font.quit()

    def test_update_game_mode(self):
        pygame.font.init()
        test_game = Game()
        test_game.update_game_mode('Multiplayer')
        self.assertFalse(test_game.entities_dict['enemy'].is_npc)

        test_game.update_game_mode('Single Player')
        self.assertTrue(test_game.entities_dict['enemy'].is_npc)
        pygame.font.quit()

    def test_check_collision(self):
        pygame.font.init()
        self.test_game = Game()

        # don't colliding
        self.test_game.check_collision()
        self.assertFalse(self.test_game.entities_dict['ball'].is_colliding)

        # enemy position
        self.test_game.entities_dict['ball'].rect.top = \
            self.test_game.entities_dict['enemy'].rect.top 

        # colliding with enemy
        self.test_game.check_collision()
        self.assertTrue(self.test_game.entities_dict['ball'].is_colliding)

        pygame.font.quit()

    def test_check_goal(self):
        pygame.font.init()
        self.test_game = Game()
        
        # pleyer goal
        self.test_game.entities_dict['ball'].rect.top = 0
        self.assertTrue(self.test_game.check_goal())

        #enemy goal
        self.test_game.entities_dict['ball'].rect.bottom = 400
        self.assertTrue(self.test_game.check_goal())
        pygame.font.quit()


class TestScoreboard(unittest.TestCase):
    test_scoreboard: Scoreboard

    def test_mark_score(self):
        pygame.font.init()
        self.test_scoreboard = Scoreboard()
        
        self.test_scoreboard.mark_score(None)
        self.assertEqual(self.test_scoreboard.player_score['score'], 0)
        self.assertEqual(self.test_scoreboard.enemy_score['score'], 0)

        self.test_scoreboard.mark_score('player')
        self.assertEqual(self.test_scoreboard.player_score['score'], 1)

        self.test_scoreboard.mark_score('enemy')
        self.assertEqual(self.test_scoreboard.enemy_score['score'], 1)
        pygame.font.quit()


if __name__ == '__main__':
    unittest.main()