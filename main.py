# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

import random

from constants import *
from circleshape import CircleShape

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Class Groups
    Player.containers = drawable, updatable
    Asteroid.containers = asteroids, drawable, updatable
    AsteroidField.containers = updatable
    Shot.containers = shots, drawable, updatable

    # CREATE PLAYER
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # CREATE ASTEROID FIELD
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((14, 14, 14))

        for element in updatable:
            element.update(dt)

        for element in asteroids:
            if player.collides_with(element):
                print("Game Over!")
                pygame.event.post(pygame.event.Event(pygame.QUIT))

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
