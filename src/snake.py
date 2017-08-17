import pygame


class Snake:
    """Snake class. The snake updates and draws itself."""
    def __init__(self, coords):
        """Snake initialiation.
        Class variables:
        self.direction -- The direction where the snake is going, 'L' etc.
        self.body -- a list of int tuples where the snake's body currently is.
        Arguments:
        coords -- The starting position of the snake, int tuple
        """
        # Now the starting direction is always right. Might be improved
        # to allow this to be changed.
        self.direction = 'R'
        # In the beginning, the body is just one element long.
        self.body = coords

    def set_x_y(self):
        """Update x and y based on direction where the snake is going.
        x and y correspond to direction changes in x and y axes.
        E.g., x = 1 and y = 0 means move one step to the right.
        Returns:
        x, y -- (int) direction changes in x and y axes (-1, 0 or 1)
        """
        if self.direction == 'U':
            x = 0
            y = -1
        if self.direction == 'D':
            x = 0
            y = 1
        if self.direction == 'R':
            x = 1
            y = 0
        if self.direction == 'L':
            x = -1
            y = 0
        return x, y

    def update(self, n, m, apple):
        """Snake update method.
        Status, direction and possible death are processed here.
        Arguments:
        n,m -- The logical size of the playfield
        apple -- Where is the apple atm, tuple (int,int)
        Returns:
        status -- (int) 0: normal, 1: ate apple, 2: died
        """
        status = 1
        # Update the coordinate changes based on where the snake is headed
        x, y = self.set_x_y()
        # b is the last element of the list body, means the snake's head
        b = self.body[-1]
        # This is where the snake's head will be next
        b = (b[0] + x, b[1] + y)
        # If snake hits itself or outside playfield, it dies
        if b in self.body or \
           b[0] > n - 1 or \
           b[0] < 0 or \
           b[1] > m - 1 or \
           b[1] < 0:
            status = 2
            return status
        # Move one space
        self.body.append(b)
        # If snake didn't eat an apple, remove the last element of list,
        # otherwise keep it, which makes the snake longer
        if b != apple:
            self.body.pop(0)
            status = 0
        return status

    def draw(self, screen, scale):
        """The draw method for Snake.
        Arguments:
        screen -- Pygame screen where to draw
        scale -- The scale parameter used in the game
        """
        for i in self.body:
            rectangle = (i[0]*scale, i[1] * scale, scale, scale)
            pygame.draw.rect(screen, (0, 50, 0), rectangle)
