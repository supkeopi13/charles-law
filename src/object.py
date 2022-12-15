import pygame

class graduation(pygame.sprite.Sprite):
  def __init__(self):
    super(graduation, self).__init__()
    self.image = pygame.image.load("img/graduation.png")
    self.image = pygame.transform.scale(self.image, (100, 200))
    
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = 350, 150
  def update(self):
    pass