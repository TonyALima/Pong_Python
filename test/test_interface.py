import sys

sys.path.insert(0, './src')

from interface import *
import unittest
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_ESCAPE

class TestMenu(unittest.TestCase):

    def observer_function(self, command):
        self.command_observed = command

    def test_moves(self):
        pygame.font.init()
        test_menu = Menu(['button 1', 'button 2', 'button 3'])
        test_menu.subscribe(self.observer_function)

        moves = test_menu.create_moves()

        moves[K_DOWN]()
        expected_value = 1
        value = test_menu.high_light['position']
        self.assertEqual(value, expected_value)

        moves[K_UP]()
        expected_value = 0
        value = test_menu.high_light['position']
        self.assertEqual(value, expected_value)

        moves[K_RETURN]()
        expected_value = 'button 1'
        value = self.command_observed
        self.assertEqual(value, expected_value)

        moves[K_ESCAPE]()
        expected_value = 'Esc'
        value = self.command_observed
        self.assertEqual(value, expected_value)
        pygame.font.quit()

    def test_calc_size_button(self):
        pygame.font.init()
        test_menu = Menu(['button 1', 'button 2', 'button 3'])

        expected_value = (100, 50, 0)
        value = test_menu.calc_size_button(2)
        self.assertEqual(value, expected_value)
        pygame.font.quit()

if __name__ == '__main__':
    unittest.main()