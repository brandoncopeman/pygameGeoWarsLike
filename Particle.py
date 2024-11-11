import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, color, size, lifespan):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)  # Support transparency
        self.color = color
        pygame.draw.circle(self.image, self.color, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=pos)
        self.lifespan = lifespan
        self.age = 0

        # Give the particle a random velocity for a spreading effect
        self.vel_x = random.uniform(-3, 3)
        self.vel_y = random.uniform(-3, 3)

    def update(self):
        # Move the particle
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Age the particle and fade out
        self.age += 1
        if self.age >= self.lifespan:
            self.kill()  # Remove the particle when its lifespan ends
        else:
            # Fade out the particle over time
            alpha = max(0, 255 - (255 * (self.age / self.lifespan)))
            self.image.set_alpha(alpha)
