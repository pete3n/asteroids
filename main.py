# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *


def main():
    pygame.init
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((255, 255, 255))
        pygame.display.flip()


if __name__ == "__main__":
    main()
