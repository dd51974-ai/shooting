import pygame # To import pygame
import os

pygame.init() # start
path = os.path.join("/ai", "develop", "/shooting","step2_bar.py")
print(path)
screen = pygame.display.set_mode((800, 600)) # Create Display size for High and width

running = True
while running: # like for sentence
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Stop running

running.quit()