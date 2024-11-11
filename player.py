import pygame
from settings import GREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

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