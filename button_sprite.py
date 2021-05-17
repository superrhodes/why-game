import sys, pygame
import sprites
import time

color = (255, 255, 255)

class Button_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cfg = open("configure.cfg", mode = 'r+')
        values = cfg.readlines()
        self.ss = int((values[0])[0])
        cfg.close()
        self.image = pygame.image.load("assets/button1.png").convert_alpha()
        if self.ss == 0:
            self.image  = pygame.transform.scale(self.image, (23,10))
        self.rect = self.image.get_rect()
        if self.ss == 0:
            self.rect.center = (400, 117)
        else:
            self.rect.center = (1000, 280)

    def right(self, fps):
        if self.ss == 0:
            self.rect.x -= 40/fps
        else:
            self.rect.x -= 100/fps
            
    def left(self, fps):
        if self.ss == 0:
            self.rect.x += 40/fps
        else:
            self.rect.x += 100/fps
    
    def press(self):
        self.image = pygame.image.load("assets/button2.png").convert_alpha()
        if self.ss == 0:
            self.image  = pygame.transform.scale(self.image, (23,10))


button_sprite = Button_Sprite()
sprites.all_sprites.add(button_sprite)