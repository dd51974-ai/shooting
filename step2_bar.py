import pygame
from step1_window import *
pygame.init()
win = window()

width = 20
height = 20
vel = 10

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    x = window()
    y = window()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 600 - height:
        y += vel


    pygame.draw.rect(win,(255, 0, 0),(x, y, width, height))
    pygame.display.update()
pygame.quit()
