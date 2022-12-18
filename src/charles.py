import pygame, random
from math import pi
from pygame.locals import K_UP, K_DOWN

TemperatureX, TemperatureY = 310, 300
width, height = 250, 150
boxWidth, boxHeight = 200, 10
ptcTime, btnTime, pstTime = 3, 500, 10

class piston(pygame.sprite.Sprite):
  UP, DOWN = 0, 0
  move, limit = 1, 20
  def __init__(self):
    super(piston, self).__init__()
    self.image = pygame.Surface((140, 10))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = (width-65, height)
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
  ptcUpdate = 0
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
      random.uniform(pistonSprite.sprite.rect.x+boxHeight+5, pistonSprite.sprite.rect.x+boxWidth-55),
      random.uniform(pistonSprite.sprite.rect.y+boxHeight+5, height+boxWidth-5)
    )
  def update(self):
    pstPos = (pistonSprite.sprite.rect.x, pistonSprite.sprite.rect.y)
    self.ptcUpdate = (self.ptcUpdate+1)%ptcTime
    if self.ptcUpdate==0:
      self.rect.x += self.dr[0][self.drIndex]
      self.rect.y += self.dr[1][self.drIndex]
      if pstPos[0]>self.rect.x:
        self.drIndex = random.randint(1, 3)
      if pstPos[1]+10>self.rect.y:
        self.drIndex = random.randint(3, 5)
      if pstPos[0]+130<self.rect.x:
        self.drIndex = random.randint(5, 7)
      if height+190<self.rect.y:
        self.drIndex = random.randint(7, 9)%8
  
class beaker(pygame.sprite.Sprite):
  def __init__(self):
    super(beaker, self).__init__()
    self.image = pygame.Surface([160, 210])
    self.image.fill((255, 255, 255))
    pygame.draw.rect(self.image, (0, 0, 0), [(0, 0), (boxHeight, boxWidth)])
    pygame.draw.rect(self.image, (0, 0, 0), [(150, 0), (boxHeight, boxWidth)])
    pygame.draw.rect(self.image, (0, 0, 0), [(0, boxWidth), (boxWidth-40, boxHeight)])
    self.rect = self.image.get_rect()
    self.rect.topleft = (250-75, 150)
  def update(self):
    pass
  
class Temperature(pygame.sprite.Sprite):
  angle, time, rotateTime = 150, 0, 100
  def __init__(self, boxSize, pos):
    super(Temperature, self).__init__()
    self.image = pygame.Surface(boxSize)
    self.image.fill((255, 255, 255))
    self.size, self.position = boxSize, pos
    pygame.draw.arc(self.image, (255, 0, 0), [(0, 0), boxSize], 0, pi*2, 2)
    pygame.draw.rect(self.image, (255, 0, 0), [(boxSize[0]/2, 47.5), (40, 5)])
    pygame.draw.circle(self.image, (0, 0, 0), (boxSize[0]/2, boxSize[1]/2), 5)
    self.rotateImage = pygame.transform.rotate(self.image, self.angle)
    self.rect = self.rotateImage.get_rect()
    self.rect.center = self.position
  def update(self, screen):
    self.angle = pistonSprite.sprite.rect.y-150
    self.rotateImage = pygame.transform.rotate(self.image, self.angle)
    self.x, self.y = self.rotateImage.get_size()
    self.position[0] = TemperatureX-(self.x/2-self.size[0])
    self.position[1] = TemperatureY-(self.y/2-self.size[1])
    screen.blit(self.rotateImage, self.position)

def charlesInit():
  global pistonSprite, rotateBoxSprite
  pistonSprite = pygame.sprite.GroupSingle(piston())
  rotateBoxSprite = pygame.sprite.GroupSingle(Temperature((100, 100), [TemperatureX, TemperatureY]))
  
def charlesExecute(screen):
  pistonSprite.update()
  pistonSprite.draw(screen)
  rotateBoxSprite.update(screen)
  font = pygame.font.SysFont(None, 30)
  text = font.render("Temperature", True, (0, 0, 0))
  screen.blit(text, (TemperatureX+40, TemperatureY+170))