import sys
sys.path.insert(0, './src')


from pygame.locals import *
import pygame
import unittest
import entities
import pygame.event

pygame.init()

class TestPlayer(unittest.TestCase):
    def test_move(self):
        test_player = entities.Player()

        expected_position = test_player.rect.center[0]
        test_player.move()
        self.assertEqual(test_player.rect.center[0], expected_position)

        expected_position -= 5
        test_player.move(left=True)
        self.assertEqual(test_player.rect.center[0], expected_position)

        expected_position += 5
        test_player.move(right=True)
        self.assertEqual(test_player.rect.center[0], expected_position)


if __name__ == '__main__':
    unittest.main()

