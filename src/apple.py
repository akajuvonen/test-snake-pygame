import pygame

from random import randint


class Apple:
    """Apple class for snake game. Requires pygame at this point."""
    def __init__(self, coords):
        """Initialization for Apple.
        Class variables:
        self.location -- The logical coordinates of the apple's position
        Arguments:
        coords -- Coordinates where the apple first appears
        """
        self.location = coords

    def update(self, snake, n, m):
        """Updates a new location for the apple after it's eaten.
        The location is recreated until the apple appears outside of snake's
        body.
        Arguments:
        snake -- Snake class instance of the game
        n,m -- The logical size (not pixels) of the playfield
        """
        while 1:
            x = randint(0, n-1)
            y = randint(0, m-1)
            if (x, y) not in snake:
                self.location = (x, y)
                break

    def draw(self, screen, scale):
        """The apple draws itself.
        Arguments:
        screen -- The PyGame screen where drawing happens
        scale -- The scale parameter of the game,
                 scales the locations to more pixels
        """
        loc = self.location
        rectangle = (loc[0]*scale, loc[1]*scale, scale, scale)
        pygame.draw.rect(screen, (100, 0, 0), rectangle)
