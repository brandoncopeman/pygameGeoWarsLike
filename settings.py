import random
import pygame
import os
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Simple Game - Vampire Survivors Style")

# Initialize the font module
pygame.font.init()
font = pygame.font.Font(None, 36)  # Use the default font and set the size to 36

tilesFolder = "tiles"
tile_images = []
for filename in os.listdir(tilesFolder):
    if filename.endswith(".png"):  # Assuming tile images are in PNG format
        tile_image = pygame.image.load(os.path.join(tilesFolder, filename)).convert()
        tile_image = pygame.transform.scale(tile_image, (50, 50))
        tile_images.append(tile_image)

def draw_tiled_floor():
    """Draw the tiled floor to cover the entire screen."""
    # Use nested loops to draw each tile in a grid pattern
    floor_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    for y in range(0, SCREEN_HEIGHT, 50):
        for x in range(0, SCREEN_WIDTH, 50):
            tile_image = random.choice(tile_images)
            # Blit (draw) the tile at each (x, y) position without scaling
            floor_surface.blit(tile_image, (x, y))
    return floor_surface