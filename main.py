import pygame
from src.charles import charles

def main():
  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  pygame.display.set_caption('Charles\'s law')

  charles(screen)
  
if __name__=="__main__":
  main()
  pygame.quit()