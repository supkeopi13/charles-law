import pygame, random
from pygame.locals import K_MINUS, K_UNDERSCORE, K_PLUS, K_EQUALS
from src.charles import *
from src.dashboard import *
from src.object import drawImage, drawSurface

btnClickedPlus = btnClickedMinus = 0

def main():
  screen = pygame.display.set_mode((500, 500))
  pygame.display.set_caption('Charles\'s law')
  charlesInit()
  dashboardInit()
  charlesLawSprites = pygame.sprite.Group([
    beaker(),
    drawImage("img/fire.png", (100, 150), (260, 450)),
    drawSurface((111, 78, 55), (100, 10), (260, 495)),
    particle()
  ])
  global btnClickedMinus, btnClickedPlus
  running = True
  while running:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running = False
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_EQUALS] or pressed_keys[K_PLUS]:
      btnClickedPlus = (btnClickedPlus+1)%btnTime
      if btnClickedPlus==0:
        charlesLawSprites.add(particle())
    if pressed_keys[K_UNDERSCORE] or pressed_keys[K_MINUS]:
      btnClickedMinus = (btnClickedMinus+1)%btnTime
      if btnClickedMinus==0 and len(charlesLawSprites)>4:
        spriteList = charlesLawSprites.sprites()
        charlesLawSprites.remove(spriteList[random.randint(3, len(spriteList)-1)])
    charlesLawSprites.update()
    screen.fill((255, 255, 255))
    charlesLawSprites.draw(screen)
    charlesExecute(screen)
    dashboardExecute(screen)
    pygame.display.flip()
  
if __name__=="__main__":
  pygame.init()
  main()
  pygame.quit()