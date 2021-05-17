import sys, pygame
from pygame.locals import *
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.font.init()

import time
import sprites
from text import *

print("Why does this exist? Version 1.5")

cfg = open("configure.cfg", mode = 'r+')
values = cfg.readlines()

ss = int((values[0])[0])
lf = int((values[1])[0])

if ss == 0:
    size = width, height = 320, 200
else:
    size = width, height = 800, 480

cfg.close()

color = 66, 158, 245
fps = 0

screen = pygame.display.set_mode(size)
icon = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

from world import *
from player_sprite import *
from button_sprite import *

while 1:
    def refresh():
        start = time.time()
        if lf == 1:
            if ss == 0:
                time.sleep(0.033333333333333)
            else:
                time.sleep(0.016666666666666)
            screen.fill(color)
        screen.blit(background, backrect)
        sprites.all_sprites.update()
        sprites.all_sprites.draw(screen)
        global fps
        try:
            fps = int(round(1.0/(time.time() - start), 0))
        except ZeroDivisionError():
            print("whoops!")
            pass

        textsurface = myfont.render(str(fps)+" fps", False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
        pygame.display.flip()

    def collision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            button_sprite.press()
            for i in range(42):
                player_sprite.rect.y -= (10-(i/2))
                if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed() [pygame.K_a]:
                    player_sprite.right(button_sprite, fps)
                    player_sprite.image = pygame.transform.rotate(player_sprite.image, -(10-(i/2)))

                if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed() [pygame.K_d]:
                    player_sprite.left(button_sprite, fps)
                    player_sprite.image = pygame.transform.rotate(player_sprite.image, (10-(i/2)))
                refresh()
            else:
                player_sprite.rect.y -= 0.5
                refresh()
            return 1

    pygame.event.set_allowed([QUIT, KEYDOWN])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(42):
                    player_sprite.rect.y -= (10-(i/2))
                    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed() [pygame.K_a]:
                        player_sprite.left(button_sprite, fps)
                        sky_sprite.left(fps)
                        grass_sprite.left(fps)
                        dirt_sprite.left(fps)
                        button_sprite.left(fps)



                    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed() [pygame.K_d]:
                        player_sprite.right(button_sprite, fps)
                        sky_sprite.right(fps)
                        grass_sprite.right(fps)
                        dirt_sprite.right(fps)
                        button_sprite.right(fps)

                        pygame.transform.rotate(player_sprite.image, (10-(i/2)))
                    refresh()
                else:
                    player_sprite.rect.y -= 0.5
                    refresh()
            elif event.key == pygame.K_LEFT:
                player_sprite.rleft()
            elif event.key == pygame.K_RIGHT:
                player_sprite.rright()
            elif event.key == pygame.K_a:
                player_sprite.rleft()
            elif event.key == pygame.K_d:
                player_sprite.rright()


    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed() [pygame.K_a]:
        player_sprite.left(button_sprite, fps)
        sky_sprite.left(fps)
        grass_sprite.left(fps)
        dirt_sprite.left(fps)
        button_sprite.left(fps)


    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed() [pygame.K_d]:
        player_sprite.right(button_sprite, fps)
        sky_sprite.right(fps)
        grass_sprite.right(fps)
        dirt_sprite.right(fps)
        button_sprite.right(fps)



    colvar = collision(player_sprite, button_sprite)
    if colvar == 1:
        break

    
    refresh()
