import pygame

from random import randint

class Apple:

    def __init__(self,coords):
        self.location = coords

    def update(self,snake,n,m):
        while 1:
            x = randint(0,n-1)
            y = randint(0,m-1)
            if (x,y) not in snake: self.location=(x,y); break;

    def draw(self,screen,scale):
        loc = self.location
        rectangle = (loc[0]*scale,loc[1]*scale,scale,scale)
        pygame.draw.rect(screen,(100,0,0),rectangle)

