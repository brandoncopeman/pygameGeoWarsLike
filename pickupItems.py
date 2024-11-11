import pygame
import random
from settings import *

class PickupItem(pygame.sprite.Sprite):
    """Represents an item that drops after every 10 kills with a shiny effect."""
    def __init__(self, position):
        super().__init__()
        
        # Determine color with a 50/50 chance
        if random.choice([True, False]):
            self.color = (255, 0, 255)  # Purple color for special effect
            self.is_purple = True
        else:
            self.color = (0, 255, 255)  # Cyan color for normal effect
            self.is_purple = False

        # Base item image
        self.base_image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.base_image.fill(self.color)
        self.rect = self.base_image.get_rect(center=position)
        
        # Shine overlay (a white gradient to transparent)
        self.shine_overlay = pygame.Surface((40, 30), pygame.SRCALPHA)
        for x in range(self.shine_overlay.get_width()):
            for y in range(self.shine_overlay.get_height()):
                alpha = max(0, 255 - (x + y) * 5)
                self.shine_overlay.set_at((x, y), (255, 255, 255, alpha))
        
        # Shine position variables
        self.shine_pos = -self.rect.width
        self.shine_speed = 2

        # Set the initial image to base_image (with no shine)
        self.image = self.base_image.copy()

    def update(self):
        # Reset the image each update
        self.image = self.base_image.copy()
        
        # Update shine position
        self.shine_pos += self.shine_speed
        if self.shine_pos > self.rect.width:
            self.shine_pos = -self.rect.width  # Reset position for continuous shine effect

        # Blit the shine overlay onto the base image at the current shine position
        self.image.blit(self.shine_overlay, (self.shine_pos, 0), special_flags=pygame.BLEND_RGBA_ADD)
