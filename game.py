import random
import pygame
from settings import *
from player import Player 
from enemy import Enemy 
from gameover import show_game_over_screen
from Particle import Particle

def start_game():
    # Set up sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()  # New player group
    particles = pygame.sprite.Group()  # Group for particles


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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    player.shoot(mouse_pos)

        # Get the state of keys
        keys = pygame.key.get_pressed()

        # Update the player and enemies
        player.update(keys)  # Manually pass the keys to the player's update method
        player.projectiles.update()
        
        for enemy in enemies:
            enemy.update()  # No need to pass keys for enemies
            
        particles.update()
            
        # Check for collisions between projectiles and enemies
        hits = pygame.sprite.groupcollide(player.projectiles, enemies, False, False)
        
        # Process each collision and create particles for each collision
        for projectile, hit_enemies in hits.items():
            # Remove the projectile
            projectile.kill()
            # Remove each enemy that was hit
            for enemy in hit_enemies:
                enemy.kill()
            for _ in range(10):  # Number of particles in each burst
                    particle = Particle(
                        pos=enemy.rect.center,
                        color=(255, 0, 0),  # Red color for the effect
                        size=random.randint(3, 6),  # Random size for variety
                        lifespan=30  # Lifespan of each particle
                    )
                    particles.add(particle)


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
        player.projectiles.draw(screen)  # Draw projectiles separately
        particles.draw(screen)

    

        # Draw the timer on the screen
        screen.blit(timer_text, timer_rect)

        # Refresh the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Show the game over screen
    show_game_over_screen(elapsed_time, clock)

