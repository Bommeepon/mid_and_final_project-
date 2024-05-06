import pygame
from setting import screen_width, screen_height, tile_size


#負責處裡顯示文字的


class Word:
    def __init__(self,surface):
        self.width = screen_width
        self.height = screen_height
        self.image = pygame.image.load('background_image/title_screen_background.png')
        self.scale_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.surface = surface
        self.font = pygame.font.Font('font/Annotated.ttf', 36)
        self.text = self.font.render('遊戲結束! 別放棄再加油!', True ,(255,255,255))
        self.border_text = self.font.render('遊戲結束! 別放棄再加油!', True ,(0,0,0))
        self.text2 = self.font.render('【按下空白鍵重新開始唷】', True ,(255,255,255))
        self.border_text2 = self.font.render('【按下空白鍵重新開始唷】', True ,(0,0,0))
        

        #通關頁面的字
        self.text_c1 = self.font.render('恭喜通關! 傻逼! 再玩一次吧!', True ,(255,255,255))
        self.border_text_c1 = self.font.render('恭喜通關! 傻逼! 再玩一次吧!', True ,(0,0,0))


        

    def fail(self):
        
        #self.surface.blit(self.scale_image,(0,0))
        #重疊形成描邊
        self.surface.blit(self.border_text, (301, 100))  # 右下方
        self.surface.blit(self.border_text, (299, 100))  # 左下方
        self.surface.blit(self.border_text, (300, 101))  # 右上方
        self.surface.blit(self.border_text, (300, 99))   # 左上方

        self.surface.blit(self.text, (300, 100))

        self.surface.blit(self.border_text2, (271, 200)) 
        self.surface.blit(self.border_text2, (269, 200))   
        self.surface.blit(self.border_text2, (270, 201))  
        self.surface.blit(self.border_text2, (270, 199))

        self.surface.blit(self.text2, (270, 200))





class Congratulation(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('background_image/con_word.png')    
        self.rect = self.image.get_rect(midtop = pos)

    def update(self,x_shift):
        self.rect.x += x_shift
        

