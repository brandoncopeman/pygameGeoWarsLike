import pygame
from settings import *

class AlternateSpecialProjectiles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load the initial image and set up for scaling
        self.original_image = pygame.image.load("assets/projectile.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (350, 350))  # Start small
        self.image = self.original_image.copy()  # Set initial display image
        self.rect = self.image.get_rect(center=(x, y))
        self.expansion_rate = 20  # Pixels to expand each frame

    def update(self):
        # Calculate the new size by adding the expansion rate
        new_size = (self.rect.width + self.expansion_rate, self.rect.height + self.expansion_rate)
        
        # Scale the image to the new size
        self.image = pygame.transform.scale(self.original_image, new_size)
        
        # Update the rect to be centered on the screen
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Remove the projectile if it fills the screen
        if self.rect.width >= SCREEN_WIDTH or self.rect.height >= SCREEN_HEIGHT:
            self.kill()  # Remove from screen when it fills the screen
