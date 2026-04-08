import pygame # To import pygame

def window():
    pygame.init()  # start
    screen = pygame.display.set_mode((800, 600))  # Create Display size for High and width
    pygame.display.set_caption("Shooting!")

    running = True
    while running:  # like for sentence
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop running
    running.quit()

if __name__ == "__main__":
    window()