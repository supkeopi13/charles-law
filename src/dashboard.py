import pygame
from math import pi

PressureX, PressureY = 100, 400

class Pressure(pygame.sprite.Sprite):
  angle, time, rotateTime = 270, 0, 100
  def __init__(self, boxSize, pos):
    super(Pressure, self).__init__()
    self.image = pygame.Surface(boxSize)
    self.image.fill((255, 255, 255))
    self.size, self.position = boxSize, pos
    pygame.draw.arc(self.image, (0, 0, 255), [(0, 0), boxSize], 0, pi*2, 2)
    pygame.draw.rect(self.image, (0, 0, 255), [(boxSize[0]/2, 47.5), (40, 5)])
    pygame.draw.circle(self.image, (0, 0, 0), (boxSize[0]/2, boxSize[1]/2), 5)
    self.rotateImage = pygame.transform.rotate(self.image, self.angle)
    self.rect = self.rotateImage.get_rect()
    self.rect.center = self.position
  def update(self, screen):
    self.angle = 90
    self.rotateImage = pygame.transform.rotate(self.image, self.angle)
    screen.blit(self.rotateImage, self.position)
    
def dashboardInit():
  global PressureSprite
  PressureSprite = pygame.sprite.GroupSingle(Pressure((100, 100), [50, 350]))
  
def dashboardExecute(screen):
  PressureSprite.update(screen)
  font = pygame.font.SysFont(None, 30)
  text1 = font.render("Pressure", True, (0, 0, 0))
  text2 = font.render("13.05", True, (0, 0, 0))
  screen.blit(text2, (PressureX-25, PressureY+10))
  screen.blit(text1, (PressureX-40, PressureY+70))