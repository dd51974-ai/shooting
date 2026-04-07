import pygame
import os

pygame.init()
win = os.path.join("/ai", "develop", "/shooting","step1_window.py")


x = 800
y = 600

width = 20
height = 20
vel = 10
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 600 - height:
        y += vel

    #win.fill((0, 0, 0))
    pygame.draw.rect(win,(255, 0, 0),(x, y, width, height))
    pygame.display.update()
pygame.quit()
