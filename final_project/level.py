import pygame
from tiles import Tile
from setting import tile_size , screen_width 
from player import Player
from portal import Portal
from dragon import Dragon
from word import Word, Congratulation
from monster import Monster
from item import Item

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface

        self.world_shift = 0 
        self.current_x = 0
        
        self.levels = level_data
        self.current_level_index = 0
        self.setup_level(self.levels[self.current_level_index])
        self.bgm1 = pygame.mixer.Sound('music/background_music.mp3')
        self.bgm2 = pygame.mixer.Sound('music/background_music2.mp3')
        self.collide_monster_sound = pygame.mixer.Sound('sound_effects/collide_monster.mp3')
        self.bgm_list = [self.bgm1,self.bgm2]
        self.bgm_index = 0
        self.fall_sound = pygame.mixer.Sound('sound_effects/fall.wav')
        #print(self.bgm1)  
        #print(self.bgm2)
        
        self.bgm_list[self.bgm_index].play(loops = -1)

        self.game_active = True
        self.ignore_tile_collision = True
        self.ignore_monster_collision = True
        self.item_timer = 0
        self.score_timer = 0
        self.score = 0
        

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.dragons = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        
        self.con_words = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tile_size 
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'R':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    portal = Portal((x,y),tile_size)
                    self.portals.add(portal)
                if cell == 'D':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    dragon = Dragon((x,y))
                    self.dragons.add(dragon)
                if cell == 'M':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    y = y + 15
                    monster = Monster((x,y))
                    self.monsters.add(monster)
                if cell == 'W':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    word = Congratulation((x,y),36)
                    self.con_words.add(word)
                if cell == 'I':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    item = Item((x,y))
                    self.items.add(item)
                           

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4  and direction_x < 0: 
            self.world_shift = 8
            player.speed = 0
        elif player_x >screen_width * 3 / 4 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6


    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
    
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): 
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right + 5
                    player.on_left = True
                    self.current_x  = player.rect.left
                elif player.direction.x >0:
                    player.rect.right = sprite.rect.left - 5
                    player.on_right = True
                    self.current_x  = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0 ):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

                    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        if self.ignore_tile_collision:
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top -1.5
                        player.direction.y = 0 
                        player.on_ground = True
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                        player.on_celling = True
                
        if player.on_ground == True and player.direction.y > 1 or player.direction.y < 0: 
            player.on_ground = False
        elif player.on_celling == True and player.direction.y > 0 :
            player.on_celling = False
    

    def portal_collision(self):
        
        player = self.player.sprite
        portals = self.portals.sprites()
        if pygame.sprite.spritecollide(player, portals, False):
            
            self.current_level_index = (self.current_level_index + 1) % len(self.levels)
            
            self.setup_level(self.levels[self.current_level_index])
            self.bgm_list[self.bgm_index].stop()
            self.bgm_index = (self.bgm_index + 1) % len(self.bgm_list)
            self.bgm_list[self.bgm_index].play(loops = -1)

            self.score = self.score_timer

            print(f'你的通關時間是{self.score:5.2f}秒')


    def monster_collision(self):
        player = self.player.sprite
        monsters = self.monsters.sprites()
        
        if self.ignore_monster_collision:
            if pygame.sprite.spritecollide(player, monsters, False):
                self.collide_monster_sound.play()
                self.game_active = False
                self.detect_active()
                self.ignore_tile_collision = False
                self.ignore_monster_collision = False
                
    def item_collision(self):
        player = self.player.sprite
        items = self.items.sprites()
       
        collided_items = pygame.sprite.spritecollide(player,items, False)
        for item in collided_items:
            self.items.remove(item)
                        
        if collided_items:               
            player.jump_speed = -30
                        
          
        if player.jump_speed < -15 :
            if self.item_timer <= 300: 
                self.item_timer += 1
            else:
                self.item_timer = 0
                player.jump_speed = -15
        

    def outside_of_map(self):
        player = self.player.sprite
        if player.rect.top >=800:
            self.game_active = False
            self.detect_active()
            

    def detect_active(self):
        if self.game_active :
            pass
        else:
            self.back_to_title()

        
    def back_to_title(self):
        word = Word(self.display_surface)
        keys = pygame.key.get_pressed()
        word.fail()
        if keys[pygame.K_SPACE]:
            self.game_active = True
            self.ignore_tile_collision = True
            self.ignore_monster_collision = True
            self.setup_level(self.levels[self.current_level_index])
            self.score_timer = 0
            
       
    def run(self):

        self.score_timer += (1/60)


        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #portal
        self.portals.update(self.world_shift)
        self.portals.draw(self.display_surface)
        self.portal_collision() 

        #dragon
        self.dragons.update()
        self.dragons.draw(self.display_surface)

        #monster
        self.monsters.update(self.world_shift)
        self.monsters.draw(self.display_surface)
        self.monster_collision()

        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        #word
        self.con_words.update(self.world_shift)
        self.con_words.draw(self.display_surface)
        #item       
        self.items.update(self.world_shift)
        self.items.draw(self.display_surface)
        self.item_collision()
        #ㄏㄏ
        
        self.outside_of_map()
        

        
        

        
        

