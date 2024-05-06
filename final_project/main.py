import pygame ,sys
from setting import *
from tiles import Tile
from level import Level
from portal import Portal

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('超好玩遊戲')
clock = pygame.time.Clock()

background_image = pygame.image.load('background_image/title_screen_background.png')  
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

level = Level(all_levels,screen) 

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)
