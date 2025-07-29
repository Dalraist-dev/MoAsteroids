#!/usr/bin/python3

#Imports
import pygame
from pygame.locals import *
from constants import *
from player import Player

# Main Functions & Methods

def main():
    
    # Game Initiation Variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Sprite Updates
        updatable.update(dt)

        # Screen Refresh/Draw   
        screen.fill("black")

        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000


# Keep at End of File

if __name__ == "__main__":
    main()