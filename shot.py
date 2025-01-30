import pygame

from circleshape import CircleShape

from constants import BULLET_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, 2)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, BULLET_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
        if (
            self.position.x < 0
            or self.position.x > SCREEN_WIDTH
            or self.position.y < 0
            or self.position.y > SCREEN_HEIGHT
        ):
            self.kill()
