import pygame
from support import import_folder

class Dragon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_dragon_assets()
        self.frame_index = 0
        self.total_frames = 114
        self.frame_rate = 60
        self.animation_duration = 9.0
        self.animation_speed = self.total_frames / (self.frame_rate * self.animation_duration)
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def import_dragon_assets(self):
        dragon_path = 'graphics/tooth_C'
        self.animations = import_folder(dragon_path)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0

        self.image = self.animations[int(self.frame_index)]
        
    def update(self):
        self.animate() 



     


