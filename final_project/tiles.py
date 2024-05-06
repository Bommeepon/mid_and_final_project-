import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('graphics/block/iron_block.png')
        self.rect = self.image.get_rect(midtop = pos)
        

    def update(self,x_shift):
        self.rect.x += x_shift
        
