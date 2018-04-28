import sys
sys.path.insert(0,'Core')

import pygame
from globalData import *
import BaseObject
import game

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

quit_attempt = False
clock = pygame.time.Clock()
gameRoom = game.GameClass(screen)

pygame.mouse.set_visible(0)
while quit_attempt != True:
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        # This part is for mouse event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse[event.button] = 1
            mouse[0] = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse[event.button] = 0
            mouse[0] = event.pos
        elif event.type == pygame.MOUSEMOTION:
            mouse[0] = event.pos
        elif event.type == pygame.KEYDOWN:
            keys[event.key % 255] = 1
        elif event.type == pygame.KEYUP:
            keys[event.key % 255] = 0
        # this part can be use for other key event.
    screen.fill(BLACK)
    dt = clock.tick(30)
    for obj in listObject:
        obj.Update()
        if obj.sprite:
            obj.DrawSprite()

    pygame.display.flip()
