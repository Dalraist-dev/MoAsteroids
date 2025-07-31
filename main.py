#!/usr/bin/python3

# Dal = Items I went off script from Project

#Imports
import sys
import time
import pygame
from pygame.locals import * # Dal
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Containers
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Player & Enviroment Initialization
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Sprite Updates
        updatable.update(dt)

        # Collision Check
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                pygame.display.set_caption("Game Over!") # Dal - Place Holder for Text on Screen - Quick Addition until I am in mood to play with Stylish Text. Wiki made it look straightforward for future projects. 
                time.sleep(5) # Dal - Too Jarring on Eyes to immediately close
                sys.exit()
        
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

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