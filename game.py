import pygame
from settings import *
from player import Player
from enemy import Enemy 
from gameover import show_game_over_screen

def start_game():
    # Set up sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()  # New player group

    # Create player
    player = Player()
    all_sprites.add(player)
    players.add(player)  # Add player to the player group

    # Create some enemies
    for _ in range(5):  # Create 5 enemies
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Track the start time of the game
    start_time = pygame.time.get_ticks()

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the state of keys
        keys = pygame.key.get_pressed()

        # Update the player and enemies
        player.update(keys)  # Manually pass the keys to the player's update method
        for enemy in enemies:
            enemy.update()  # No need to pass keys for enemies

        # Check for collisions between the player and enemies
        if pygame.sprite.spritecollideany(player, enemies):
            running = False  # End the game if a collision is detected

        # Calculate the elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert to seconds

        # Render the timer
        timer_text = font.render(f"Time Survived: {elapsed_time} seconds", True, BLACK)
        timer_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, 20))

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the timer on the screen
        screen.blit(timer_text, timer_rect)

        # Refresh the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Show the game over screen
    show_game_over_screen(elapsed_time, clock)

