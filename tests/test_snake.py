import unittest
from snake import Snake


class SnakeTest(unittest.TestCase):
    def test_set_x_y(self):
        """Test that snake x and y coordinates correctly updated."""
        snake = Snake([0, 0])
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

    def test_check_death(self):
        """Test that snake's death correctly processed."""
        snake = Snake([(2, 2), (2, 1)])
        n, m = 2, 2
        # Update the coordinate changes based on where the snake is headed
        x, y = snake.set_x_y()
        # b is the last element of the list body, means the snake's head
        b = snake.body[-1]
        # This is where the snake's head will be next
        b = (b[0] + x, b[1] + y)
        # Check if the snake dies
        self.assertTrue(snake.check_death(b, n, m))
        # Now the same when the snake should stay alive
        snake = Snake([(2, 2), (2, 1)])
        n, m = 4, 4
        # Update the coordinate changes based on where the snake is headed
        x, y = snake.set_x_y()
        # b is the last element of the list body, means the snake's head
        b = snake.body[-1]
        # This is where the snake's head will be next
        b = (b[0] + x, b[1] + y)
        # Check if the snake dies
        self.assertFalse(snake.check_death(b, n, m))

    def test_update(self):
        """Test that the update function returns the correct status"""
        # Status codes
        normal = 0
        ate_apple = 1
        died = 2
        n, m = 2, 2
        snake = Snake([(0, 1), (0, 0)])
        snake.direction = 'R'
        apple = (1, 1)
        # Normal status = 0
        status = snake.update(n, m, apple)
        self.assertEqual(status, normal)
        # Ate apple status = 1
        snake.direction = 'D'
        status = snake.update(n, m, apple)
        self.assertEqual(status, ate_apple)
        # Died status = 2
        status = snake.update(n, m, apple)
        self.assertEqual(status, died)
