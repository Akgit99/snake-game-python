import pygame, random, sys
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
FPS = 30
DISPLAYSURF = pygame.display.set_mode((600,600))
pygame.display.set_caption('CHECKING')

BLUE = (0,0,255)
GREEN = (0,255,0)
COLOR = (255,0,0)

font = pygame.font.Font('freesansbold.ttf', 40)
#TEXTSURF = font.render("HELLO SCREEN", True, (255,255,255), RED)
TEXTSURF2 = font.render("CLICK HERE",True,  (255,255,255), BLUE)
counter = 0
while True:
    DISPLAYSURF.fill((COLOR[1], COLOR[2], COLOR[0]))
    text = f'Clicked: {counter}'
    TEXTSURF = font.render(text, True, (255,255,255), COLOR)
    DISPLAYSURF.blit(TEXTSURF, (50,100))
    s = DISPLAYSURF.blit(TEXTSURF2, (50,150))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            if(s.collidepoint(event.pos)):
                color_values = [random.randint(0,255) for _ in range(3)]
                print("clicked")
                counter += 1
                COLOR = (color_values[0], color_values[1], color_values[2])
    pygame.display.update()
    fpsClock.tick(FPS)
