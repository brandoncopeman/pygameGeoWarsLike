import pygame
import math
from projectiles import Projectile
from settings import GREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/hero.png").convert_alpha()  # Load with transparency
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)  # Create a mask from the player image pixel perfect
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

        # Projectile group
        self.projectiles = pygame.sprite.Group()
        
    def update(self, keys):
        # Track movement in both x and y directions
        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed
        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
            
          # Normalize diagonal movement to maintain consistent speed
        if dx != 0 and dy != 0:
            dx *= 0.7071  # Approximately 1/sqrt(2)
            dy *= 0.7071
         # Update the player's position
        self.rect.x += dx
        self.rect.y += dy

        # Keep the player within bounds
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
        
    def shoot(self, mouse_pos):
        # Calculate the angle from the player to the mouse position
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        angle = math.atan2(dy, dx)

        # Create a new projectile moving in the direction of the mouse position
        projectile = Projectile(self.rect.centerx, self.rect.centery, angle)
        self.projectiles.add(projectile)