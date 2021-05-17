import sys, pygame
pygame.font.init()
cfg = open("configure.cfg", mode = 'r+')
values = cfg.readlines()
ss = int((values[0])[0])
cfg.close()

if ss == 0:
    myfont = pygame.font.SysFont('Arial Black', 15)
else:
    myfont = pygame.font.SysFont('Arial Black', 30)