import pygame
from pygame.constants import QUIT
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My Game')

def even_handler():
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

while True:
    even_handler()
    pygame.display.update()
