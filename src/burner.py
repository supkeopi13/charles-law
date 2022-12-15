import pygame

class wood(pygame.sprite.Sprite):
  def __init__(self):
    super(wood, self).__init__()
    self.image = pygame.Surface((100, 10))
    self.image.fill((0, 0, 0))
    '''
    self.image = pygame.image.load("img/wood.png")
    self.image = pygame.transform.scale(self.image, (100, 10))
    '''
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = 200, 490
  def update(self):
    pass

class fire(pygame.sprite.Sprite):
  def __init__(self):
    super(fire, self).__init__()
    self.image = pygame.image.load("img/fire.png")
    self.image = pygame.transform.scale(self.image, (100, 150))
    self.rect = self.image.get_rect()
    self.rect.center = (250, 450)
  def update(self):
    pass