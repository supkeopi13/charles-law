import pygame
import random
from pygame.locals import (
  K_UP, K_DOWN, 
  K_MINUS, K_UNDERSCORE, 
  K_PLUS, K_EQUALS
)

width, height = 250, 150
boxWidth, boxHeight = 200, 10
ptcTime, btnTime, pstTime = 10, 500, 15

class piston(pygame.sprite.Sprite):
  UP, DOWN = 0, 0
  move, limit = 1, 30
  def __init__(self):
    super(piston, self).__init__()
    self.image = pygame.Surface((160, 10))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = (width-75, height)
  def update(self):
    pressed_keys = pygame.key.get_pressed()
    if self.rect.y-self.move >= height and pressed_keys[K_UP]:
      self.UP = (self.UP+1)%pstTime
      if self.UP==0:
        self.rect.y -= self.move
    if self.rect.y+self.move <= height+boxWidth-self.limit and pressed_keys[K_DOWN]:
      self.DOWN = (self.DOWN+1)%pstTime
      if self.DOWN==0:
        self.rect.y += self.move

class particle(pygame.sprite.Sprite):
  dr = [
    [0, 1, 1, 1, 0, -1, -1, -1],
    [-1, -1, 0, 1, 1, 1, 0, -1]
  ]
  def __init__(self):
    super(particle, self).__init__()
    self.drIndex = random.randint(0, 7)
    self.image = pygame.Surface((10, 10))
    self.image.fill((255, 255, 255))
    pygame.draw.circle(self.image, (0, 0, 255), (5, 5), 5)
    self.rect = self.image.get_rect()
    self.rect.center = (
      random.uniform(sprite1.sprite.rect.x+boxHeight+5, sprite1.sprite.rect.x+boxWidth-55),
      random.uniform(sprite1.sprite.rect.y+boxHeight+5, height+boxWidth-5)
    )
  def update(self):
    pstPos = (sprite1.sprite.rect.x, sprite1.sprite.rect.y)
    # Move particle
    if ptcUpdate==0:
      self.rect.x += self.dr[0][self.drIndex]
      self.rect.y += self.dr[1][self.drIndex]
      if pstPos[0]+10>self.rect.x:
        self.drIndex = random.randint(1, 3)
      if pstPos[1]+10>self.rect.y:
        self.drIndex = random.randint(3, 5)
      if pstPos[0]+140<self.rect.x:
        self.drIndex = random.randint(5, 7)
      if height+190<self.rect.y:
        self.drIndex = random.randint(7, 9)%8

class burner(pygame.sprite.Sprite):
  def __init__(self):
    super(burner, self).__init__()
    self.image = pygame.image.load("img/fire.png")
    self.image = pygame.transform.scale(self.image, (100, 150))
    self.rect = self.image.get_rect()
    self.rect.center = (250, 450)
  def update(self):
    pass

def charles(screen):
  global sprite1, ptcUpdate
  sprite1 = pygame.sprite.GroupSingle(piston())
  sprite2 = pygame.sprite.GroupSingle(burner())
  spriteGroup = pygame.sprite.Group(particle())
  btnClickedPlus = btnClickedMinus = ptcUpdate = 0
  
  running = True
  while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running = False
        
    # Add & Delete particle
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_EQUALS] or pressed_keys[K_PLUS]:
      btnClickedPlus = (btnClickedPlus+1)%btnTime
      if btnClickedPlus==0:
        spriteGroup.add(particle())
    if pressed_keys[K_UNDERSCORE] or pressed_keys[K_MINUS]:
      btnClickedMinus = (btnClickedMinus+1)%btnTime
      if btnClickedMinus==0 and len(spriteGroup)>1:
        spriteList = spriteGroup.sprites()
        spriteGroup.remove(spriteList[random.randint(0, len(spriteList)-1)])
        
    # Update
    ptcUpdate = (ptcUpdate+1)%ptcTime
    sprite1.update()
    sprite2.update()
    spriteGroup.update()
    
    # Draw
    sprite2.draw(screen)
    sprite1.draw(screen)
    spriteGroup.draw(screen)
    pygame.draw.rect(screen, (0, 0, 0), [(width-75, height), (boxHeight, boxWidth)])
    pygame.draw.rect(screen, (0, 0, 0), [(width+75, height), (boxHeight, boxWidth)])
    pygame.draw.rect(screen, (0, 0, 0), [(width-75, height+boxWidth), (boxWidth-40, boxHeight)])
    pygame.draw.rect(screen, (0, 0, 0), [(200, 490), (100, 10)]) # burner
    
    pygame.display.flip()