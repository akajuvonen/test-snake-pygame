import unittest
from apple import Apple
from snake import Snake


class AppleTest(unittest.TestCase):
    def test_update(self):
        """Test that apple location is correctly updated"""
        # Logical size of the playfield
        n = 10
        m = 10
        # Create snake and apple
        snake = Snake([(1, 3), (2, 3), (3, 3)])
        apple = Apple((5, 5))
        # Update apple
        apple.update(snake, n, m)
        # Make sure apple is not outside the playfield
        self.assertTrue(0 <= apple.location[0] <= n)
        self.assertTrue(0 <= apple.location[1] <= m)
