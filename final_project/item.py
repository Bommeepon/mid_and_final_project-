import pygame
from support import import_folder
class Item(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_item_assesets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(midtop = pos )
        
    def import_item_assesets(self):
        item_path = 'graphics/item/item1'
        self.animations = import_folder(item_path)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]
        
    def update(self,x_shift):
        self.rect.x += x_shift
        self.animate() 
