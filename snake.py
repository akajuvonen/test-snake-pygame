import pygame
from pygame.locals import *
import time
import sys
from random import randint
import pickle


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


class Apple:

  location = (10,10)

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


def check_btn_press(btn,curdir):
  direction = curdir
  if btn==K_UP and curdir!='D': direction='U'
  if btn==K_DOWN and curdir!='U': direction='D'
  if btn==K_RIGHT and curdir!='L': direction='R'
  if btn==K_LEFT and curdir!='R': direction='L'
  return direction


def main():

  n,m = 30,20
  scale=25
  w,h=n*scale,m*scale
  background_color=(100,250,100)

  # Init screen
  pygame.init()
  screen = pygame.display.set_mode((w,h+scale*2))
  pygame.display.set_caption('Snake test game')

  # fill background
  background = pygame.Surface((w,h+scale*2))
  background = background.convert()
  background.fill(background_color)

  textbox = pygame.Surface.subsurface(background,(scale,h+2,scale*15,scale*2-2))
  textbox.convert()

  # Fill lines
  for i in range(0,h+scale,scale):
    pygame.draw.line(background,(0,0,0),(0,i),(w,i))
  for i in range(0,w+scale,scale):
    pygame.draw.line(background,(0,0,0),(i,0),(i,h))

  # Init text
  font = pygame.font.Font(None,35)

  # Init snake and apple
  snake = Snake([(1,3),(2,3),(3,3)])
  apple = Apple((5,5))
  apple.update(snake.body,n,m)

  # Load high score
  try:
    with open('score.dat','rb') as file:
      highscore=pickle.load(file)
  except:
    highscore=0

  # Event loop
  i=0
  ticker=20
  key=K_RIGHT
  score=0
  running=1
  try:
    while running:

      screen.blit(background,(0,0))

      textbox.fill(background_color)

      for event in pygame.event.get():
        if event.type == KEYDOWN:
          key = event.key
          if key == K_ESCAPE: running=0

      if i==ticker:
        snake.direction = check_btn_press(key,snake.direction)
        snakestatus = snake.update(n,m,apple.location)
        if snakestatus==1:
          score = score+1
          apple.update(snake.body,n,m)
          if ticker>7: ticker=ticker-1
        if snakestatus==2: running=0
        i=0

      snake.draw(screen,scale)
      apple.draw(screen,scale)

      text = font.render('Score: ' + str(score) + '  High score: ' + str(highscore),1,(0,0,0))
      textbox.blit(text,(0,0))

      pygame.display.flip()

      i=i+1
      time.sleep(0.01)

    if score>highscore:
      with open('score.dat','wb') as file:
        pickle.dump(score,file)

  finally:
    pygame.quit()


if __name__ == '__main__': main()
