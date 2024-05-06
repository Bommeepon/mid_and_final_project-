import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('graphics/portal/door.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect(midtop = pos)
        
    def update(self,x_shift):
        self.rect.x += x_shift
