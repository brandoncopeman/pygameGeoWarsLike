import pygame
import math
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("assets/projectile.png").convert_alpha()  # Load with transparency
        self.image = pygame.transform.scale(self.image, (50,50))
        self.mask = pygame.mask.from_surface(self.image)  # Create mask for pixel-perfect collision
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

        # Calculate velocity based on angle
        self.vel_x = math.cos(angle) * self.speed
        self.vel_y = math.sin(angle) * self.speed

    def update(self):
        # Move the projectile in the specified direction
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Remove the projectile if it goes off-screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
