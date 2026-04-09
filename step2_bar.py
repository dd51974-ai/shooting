import pygame

from step1_window import *
def bar():
    pygame.init()
    win = window() # def window() from step1_window

    x = 400
    y = 540

    width = 10
    height = 10
    vel = 10

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # If you change "False", you never finished
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 800 - width:
            x += vel
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 600 - height:
            y += vel

        win.fill((0, 0, 0)) # Leave no trace of Bar
        pygame.draw.rect(win,(255, 0, 0),(x, y, width, height))
        pygame.display.update()

pygame.init()
if __name__ == "__main__":
    bar()