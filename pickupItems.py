import pygame
import random
from settings import *

class PickupItem(pygame.sprite.Sprite):
    """Represents an item that drops after every 10 kills."""
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 255))  # Cyan color for visibility
        self.rect = self.image.get_rect(center=position)
