import sys, pygame
import sprites

background = pygame.image.load("assets/background.png")
backrect = background.get_rect()

background = pygame.image.load("assets/background.png")
backrect = background.get_rect()

background = pygame.image.load("assets/background.png")
backrect = background.get_rect()

class Sky_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cfg = open("configure.cfg", mode = 'r+')
        values = cfg.readlines()
        self.ss = int((values[0])[0])
        cfg.close()
        self.image = pygame.image.load("assets/sky.png").convert()
        if self.ss == 0:
            self.image  = pygame.transform.scale(self.image, (2560,213))
        self.rect = self.image.get_rect()
        if self.ss == 0:
            self.rect.center = (0, 92)
        else:
            self.rect.center = (0, 220)

    def right(self, fps):

        if self.ss == 0:
            self.rect.x -= 180/fps
            if self.rect.right < 321:
                self.rect.right = 800
        else:
            self.rect.x -= 450/fps
            if self.rect.right < 801:
                self.rect.right = 800

    def left(self, fps):
        if self.ss == 0:
            self.rect.x += 180/fps
        else:
            self.rect.x += 450/fps     
        if self.rect.left > -1:
            self.rect.left = 0

sky_sprite = Sky_Sprite()
sprites.all_sprites.add(sky_sprite)

class Grass_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cfg = open("configure.cfg", mode = 'r+')
        values = cfg.readlines()
        self.ss = int((values[0])[0])
        cfg.close()
        self.image = pygame.image.load("assets/grass.png").convert()
        if self.ss == 0:
            self.image  = pygame.transform.scale(self.image, (2560,80))
        self.rect = self.image.get_rect()
        if self.ss == 0:
            self.rect.center = (0, 150)
        else:
            self.rect.center = (0, 360)

    def right(self, fps):
        if self.ss == 0:
            self.rect.x -= 55/fps
            if self.rect.right < 321:
                self.rect.right = 800
        else:
            self.rect.x -= 100/fps
            if self.rect.right < 801:
                self.rect.right = 800

    def left(self, fps):
        if self.ss == 0:
            self.rect.x += 40/fps
        else:
            self.rect.x += 100/fps
        if self.rect.left > -1:
            self.rect.left = 0

grass_sprite = Grass_Sprite()
sprites.all_sprites.add(grass_sprite)

class Dirt_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cfg = open("configure.cfg", mode = 'r+')
        values = cfg.readlines()
        self.ss = int((values[0])[0])
        cfg.close()
        self.image = pygame.image.load("assets/dirt.png").convert()
        if self.ss == 0:
            self.image  = pygame.transform.scale(self.image, (2560,133))
        self.rect = self.image.get_rect()
        if self.ss == 0:
            self.rect.center = (0, 217)
        else:
            self.rect.center = (0, 520)

    def right(self, fps):
        if self.ss == 0:
            self.rect.x -= 60/fps
            if self.rect.right < 321:
                self.rect.right = 800
        else:
            self.rect.x -= 80/fps
            if self.rect.right < 801:
                self.rect.right = 800

    def left(self, fps):
        if self.ss == 0:
            self.rect.x += 32/fps
        else:
            self.rect.x += 80/fps
        if self.rect.left > -1:
            self.rect.left = 0

dirt_sprite = Dirt_Sprite()
sprites.all_sprites.add(dirt_sprite)