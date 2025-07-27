#!/usr/bin/python3

#Imports
import pygame
from pygame.locals import *
from constants import *

# Main Functions & Methods

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


# Keep at End of File

if __name__ == "__main__":
    main()
