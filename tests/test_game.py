import unittest
from game import check_btn_press, load_high_score
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, K_ESCAPE
import pickle
import os


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
        filename = 'score.dat'
        # If score file already exists, rename it temporarily
        if os.path.isfile(filename):
            os.rename(filename, filename + '.bak')
        # Try to load a high score from file
        highscore = load_high_score()
        # File doesn't exist so should be 0
        self.assertEqual(highscore, 0)
        # Create a high score file
        with open(filename, 'wb') as f:
            pickle.dump(999, f)
        # Load it
        highscore = load_high_score()
        # Check correct score
        self.assertEqual(highscore, 999)
        # Delete temp file
        os.remove(filename)
        # Rename score file to original if necessary
        if os.path.isfile(filename + '.bak'):
            os.rename(filename + '.bak', filename)

    def test_update_high_score(self):
        """High score update test"""
        pass
