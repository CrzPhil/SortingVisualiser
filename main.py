
import pygame
import random
import sys
import time
from pygame.locals import *

# Init
pygame.init()
# pygame.font.init()

# Font
# myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Window size
width = 900
height = 650

# Array Size
arr_size = 50

# Colours
global clr_arr
all_clrs = ["#2E77AE", "#FF8E2B", "#46F52C"]  # 0 Blue; 1 Orange; 2 Green
clr_arr = ["#2E77AE"] * arr_size


def generateArray():
    array = []

    for i in range(arr_size):
        array.append(random.randint(0, 300))

    return array


def drawScreen(screen, array):
    offset_x = 2
    offset_y = 600

    for i in range(len(array)):
        pygame.draw.line(screen, clr_arr[i], (0 + offset_x, offset_y), (0 + offset_x, offset_y - array[i]), 8)
        offset_x += 9


def refill(screen, array):
    screen.fill((255, 255, 255))
    drawScreen(screen, array)
    pygame.display.update()
    pygame.time.delay(10)


def insertionSort(screen, arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        clr_arr[i] = all_clrs[1]
        refill(screen, arr)

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            clr_arr[j] = all_clrs[1]
            refill(screen, arr)
            arr[j + 1] = arr[j]
            clr_arr[j] = all_clrs[0]
            j -= 1

        arr[j + 1] = key
        clr_arr[i] = all_clrs[0]

    return arr


def main():
    global control
    # Checks whether array already has been sorted
    control = False
    control2 = False

    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("SORTING VISUALISER")

    # Game loop
    run = True

    custom_array = generateArray()

    while run:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if not control:
            insertionSort(screen, custom_array)
        if not control2:
            for i in range(len(clr_arr)):
                clr_arr[i] = all_clrs[2]

        control = True
        control2 = True

        refill(screen, custom_array)


if __name__ == '__main__':
    main()


