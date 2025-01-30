# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from circleshape import CircleShape

from player import Player


def main():
    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((14, 14, 14))

        for element in updatable:
            element.update(dt)

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
