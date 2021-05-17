import sys, pygame
sys.path.insert(1, '../assets')
import sprites
import time

color = (255, 255, 255)

class Player_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cfg = open("configure.cfg", mode = 'r+')
        values = cfg.readlines()
        self.ss = int((values[0])[0])
        self.ms = int((values[2])[0])
        cfg.close()
        self.image = pygame.image.load("assets/player1.png").convert_alpha()
        if self.ss == 0:
            self.image  = pygame.transform.scale(self.image, (26,53))
        self.rect = self.image.get_rect()
        # self.rect.center = (60, 280)
        if self.ss == 0:
            self.rect.center = (320 / 2, 200 / 2)
        else:
            self.rect.center = (800 / 2, 480 / 2)
        self.direction = "right"
        
    def right(self, sprite2, fps):
        if self.ms == 0:
            if self.ss == 0:
                self.rect.x += 20/fps
                if self.rect.right > 320:
                    self.rect.right = 320
            else:
                self.rect.x += 50/fps
                if self.rect.right > 800:
                    self.rect.right = 800
        else:
            if self.ss == 0:
                self.rect.x += 40/fps
                if self.rect.right > 320:
                    self.rect.right = 320
            else:
                self.rect.x += 100/fps
                if self.rect.right > 800:
                    self.rect.right = 800

        col = pygame.sprite.collide_rect(self, sprite2)
        angle = 0
        i = 0
        if col == True:
            self.image = pygame.image.load("assets/player2.png").convert_alpha()
            if self.ss == 0:
                self.image  = pygame.transform.scale(self.image, (26,53))
            print("noooooo!")



    def rright(self):
        if self.direction == "right":
            return
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "right"
            
    def left(self, sprite2, fps):
        if self.ms == 0:
            if self.ss == 0:
                self.rect.x -= 20/fps   
            else:
                self.rect.x -= 50/fps
            if self.rect.left < 0:
                self.rect.x -= 20/fps
                self.rect.left = 0
        else:
            if self.ss == 0:
                self.rect.x -= 40/fps   
            else:
                self.rect.x -= 100/fps
            if self.rect.left < 0:
                self.rect.x -= 40/fps
                self.rect.left = 0
        col = pygame.sprite.collide_rect(self, sprite2)
        if col == True:
            self.image = pygame.image.load("assets/player2.png").convert_alpha()
            if self.ss == 0:
                self.image  = pygame.transform.scale(self.image, (26,53))
            print("noooooo!")

    def rleft(self):
        if self.direction == "left":
            return
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "left"


player_sprite = Player_Sprite()
sprites.all_sprites.add(player_sprite)