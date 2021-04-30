
import pygame, sys, random
from pygame.locals import *


# Init
pygame.init()
# pygame.font.init()

# Font
# myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Window size
width = 900
height = 650


def generateArray():
    size = 80
    array = []

    for i in range(size):
        array.append(random.randint(0, 300))

    return array


def drawScreen(screen, array):
    '''text = myfont.render("Hit [Enter] to start sorting!", False, (0, 0, 0))

    # Pos
    screen.blit(text, (20, 20))'''

    offset = 2

    for i in range(len(array)):
        pygame.draw.line(screen, (0, 0, 255), (5+offset, 20), (5+offset, array[i] + 20), 1)
        offset += 2


def main():
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("SORTING VISUALISER")

    # Game loop
    run = True

    custom_array = generateArray()

    while run:  # main game loop
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        drawScreen(screen, custom_array)
        pygame.display.update()


if __name__ == '__main__':
    main()


