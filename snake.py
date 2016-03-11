import pygame

class Snake:

  body = []
  direction = 'R'

  def __init__(self,coords):
    self.body = coords

  def update(self,n,m,apple):
    # 0:normal, 1: ate apple, 2: died
    status=1
    if self.direction=='U': x=0;y=-1;
    if self.direction=='D': x=0;y=1;
    if self.direction=='R': x=1;y=0;
    if self.direction=='L': x=-1;y=0;
    b = self.body[-1]
    b = (b[0]+x,b[1]+y)
    if b in self.body or b[0]>n-1 or b[0]<0 or b[1]>m-1 or b[1]<0:
      status=2
      return status
    self.body.append(b)
    if b != apple:
      self.body.pop(0)
      status=0
    return status

  def draw(self,screen,scale):
    for i in self.body:
      rectangle = (i[0]*scale,i[1]*scale,scale,scale)
      pygame.draw.rect(screen,(0,50,0),rectangle)
