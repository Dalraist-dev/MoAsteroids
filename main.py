#!/usr/bin/python3

#Imports
import pygame
from pygame.locals import *
from constants import *

# Main Functions & Methods

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

# Keep at End of File

if __name__ == "__main__":
    main()
