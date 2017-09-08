import unittest
from game import check_btn_press
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, K_ESCAPE


class GameTest(unittest.TestCase):
    def test_check_btn_press(self):
        """Test that direction changed when button pressed"""
        direction = check_btn_press(K_UP, 'R')
        self.assertEqual(direction, 'U')
        direction = check_btn_press(K_DOWN, 'R')
        self.assertEqual(direction, 'D')
        direction = check_btn_press(K_RIGHT, 'U')
        self.assertEqual(direction, 'R')
        direction = check_btn_press(K_LEFT, 'U')
        self.assertEqual(direction, 'L')

    def test_check_btn_press_negative(self):
        """Test that direction not changed opposite direction pressed"""
        direction = check_btn_press(K_UP, 'D')
        self.assertEqual(direction, 'D')
        direction = check_btn_press(K_DOWN, 'U')
        self.assertEqual(direction, 'U')
        direction = check_btn_press(K_RIGHT, 'L')
        self.assertEqual(direction, 'L')
        direction = check_btn_press(K_LEFT, 'R')
        self.assertEqual(direction, 'R')

    def test_load_high_score(self):
        """High score loading test"""
        pass

    def test_update_high_score(self):
        """High score update test"""
        pass
