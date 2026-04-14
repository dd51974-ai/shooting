import pygame

from step2_bar import *

def bullet():
    pygame.init()
    win = window()
    x = 0
    y = 1 # x and y are bullets size
    bullets = [x, y] #barrage
    bullet = []
    bullet_x = x
    bullet_y = y
    keys = pygame.key.get_pressed()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # Finish because change True to False
        if keys[pygame.K_SPACE]:
            bullets.append([x, y])
            for bullet in bullets:
                bullet[1] -= 10
        pygame.draw.rect(win, (255, 255, 255), (bullet_x[0], bullet_y[1], 5, 10))
        if bullet[1] < 0:
            bullet.remove(bullet)
        pygame.display.update()

pygame.init()
if __name__ == "__main__":
    bullet()