import pygame

class drawImage(pygame.sprite.Sprite):
  def __init__(self, image, size, position):
    super(drawImage, self).__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image, size)
    self.rect = self.image.get_rect()
    self.rect.center = position
  def update(self):
    pass
  
class drawSurface(pygame.sprite.Sprite):
  def __init__(self, color, size, position):
    super(drawSurface, self).__init__()
    self.image = pygame.Surface(size)
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.center = position
  def update(self):
    pass