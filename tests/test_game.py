import unittest
from game import check_btn_press
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, K_ESCAPE


class GameTest(unittest.TestCase):
    def test_check_btn_press(self):
        """Test that direction changed when button pressed"""
        direction = check_btn_press(K_UP, 'R')
        self.assertEquals(direction, 'U')
        direction = check_btn_press(K_DOWN, 'R')
        self.assertEquals(direction, 'D')
        direction = check_btn_press(K_RIGHT, 'U')
        self.assertEquals(direction, 'R')
        direction = check_btn_press(K_LEFT, 'U')
        self.assertEquals(direction, 'L')
