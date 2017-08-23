import unittest
from snake import Snake


class SnakeTest(unittest.TestCase):
    def test_set_x_y(self):
        """Test that snake x and y coordinates correctly updated."""
        snake = Snake(0, 0)
        # Check that x and y coordinate changes are correct
        x, y = 0, 0
        snake.direction = 'U'
        x, y = snake.set_x_y()
        self.assertEqual(x, 0)
        self.assertEqual(y, -1)
        snake.direction = 'D'
        x, y = snake.set_x_y()
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)
        snake.direction = 'R'
        x, y = snake.set_x_y()
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)
        snake.direction = 'L'
        x, y = snake.set_x_y()
        self.assertEqual(x, -1)
        self.assertEqual(y, 0)
