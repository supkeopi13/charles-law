import pygame, random
from pygame.locals import K_MINUS, K_UNDERSCORE, K_PLUS, K_EQUALS

from src.charles import *
from src.burner import fire, wood
from src.object import graduation

def main():
  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  pygame.display.set_caption('Charles\'s law')

  charles_init()
  sprite2 = pygame.sprite.Group([fire(), wood()])
  sprite3 = pygame.sprite.Group(graduation())
  spriteGroup = pygame.sprite.Group(particle())
  btnClickedPlus = btnClickedMinus = 0
  
  running = True
  while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running = False
    # Update
    sprite2.update()
    sprite3.update()
    spriteGroup.update()
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
    # from Other file
    charles_execution(screen)
    # Draw
    sprite2.draw(screen)
    sprite3.draw(screen)
    spriteGroup.draw(screen)
    pygame.draw.rect(screen, (0, 0, 0), [(width-75, height), (boxHeight, boxWidth)])
    pygame.draw.rect(screen, (0, 0, 0), [(width+75, height), (boxHeight, boxWidth)])
    pygame.draw.rect(screen, (0, 0, 0), [(width-75, height+boxWidth), (boxWidth-40, boxHeight)])
    pygame.display.flip()
  
if __name__=="__main__":
  main()
  pygame.quit()