import pygame
from support import import_folder
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
    
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
       
        self.rect = self.image.get_rect(midtop=pos)
       
    #player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -15
    #player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_celling = False
        self.on_left = False
        self.on_right = False
        

        self.jump_sound1 = pygame.mixer.Sound('sound_effects/jump.wav')
        self.jump_sound2 = pygame.mixer.Sound('sound_effects/jump2.wav')
        self.jump_sound_list = [self.jump_sound1,self.jump_sound2]
        
        
    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():

            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)           

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed 
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        image = animation[int(self.frame_index)]
        if self.facing_right:
           self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image


        if self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ground and self.on_right:         
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_celling:
            self.rect =  self.image.get_rect(midtop = self.rect.midtop)
        elif self.on_celling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_celling and self.on_right:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)        
        else:
            self.rect =  self.image.get_rect(center = self.rect.center)
           

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] and self.on_ground == True:
            self.jump()
            jump_sound = random.choice(self.jump_sound_list)
            jump_sound.play()

    def get_status(self): 
        if self.direction.y < 0 :
            self.status = 'jump'
        elif self.direction.y > 1 : 
            self.status = 'fall'
        elif self.direction.x != 0:        
            self.status = 'run'
        else:
            self.status = 'idle'


    def apply_gravity(self):
        keys = pygame.key.get_pressed()
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        

    def jump(self):
        self.direction.y = self.jump_speed
        

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
 