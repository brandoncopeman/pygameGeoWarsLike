import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        if random.choice([True, False]):
          # Spawn off the left or right side
            self.rect.x = random.choice([-self.rect.width, SCREEN_WIDTH])
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        else:
            # Spawn off the top or bottom side
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.choice([-self.rect.height, SCREEN_HEIGHT])
        #spwawn randomly 
        #self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        #self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = 3
        self.vel_x = random.choice([-1, 1]) * self.speed
        self.vel_y = random.choice([-1, 1]) * self.speed

    def update(self):
        # Adjust velocity randomly to create smoother movement
        if random.random() < 0.05:  # 5% chance to change direction
            self.vel_x = random.choice([-1, 0, 1]) * self.speed
            self.vel_y = random.choice([-1, 0, 1]) * self.speed

        # Update position based on velocity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the enemy within bounds
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.vel_x = -self.vel_x  # Reverse direction on collision with screen edge
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.vel_y = -self.vel_y  # Reverse direction on collision with screen edge

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))