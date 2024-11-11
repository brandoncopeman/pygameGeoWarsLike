import random
import pygame
from alternateSpecialProjectiles import AlternateSpecialProjectiles
from settings import *
from player import Player 
from enemy import Enemy 
from gameover import show_game_over_screen
from Particle import Particle
from titlescreen import show_title_screen
from instructions import show_instructions_screen
from pickupItems import PickupItem
from specialProjectiles import specialProjectile

def start_game():
    show_title_screen()  # Show the title screen before starting the game
    show_instructions_screen()  # Show the instructions screen before starting the game
    # Set up sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()  # New player group
    particles = pygame.sprite.Group()  # Group for particles
    pickups = pygame.sprite.Group()  # Group for pickup items
    specialPro = pygame.sprite.Group()  # Group for special projectiles
    altPro = pygame.sprite.Group()  # Group for special projectiles


    
    # Pre-render the tiled floor once
    floor_surface = draw_tiled_floor()

    # Create player
    player = Player()
    all_sprites.add(player)
    players.add(player)  # Add player to the player group

      # Create initial enemies
    initial_enemy_count = 5
    for _ in range(initial_enemy_count):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Track the start time of the game
    start_time = pygame.time.get_ticks()
    last_enemy_spawn_time = start_time
    enemies_to_spawn = initial_enemy_count  # Start with 5 enemies for the first spawn
    kills = 0
    special_projectile_ready = False  # Track if player has a special projectile
    use_alternate_special_projectile = False

    # Game loop
    running = True
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load(os.path.join(sounds_folder, "bg1.wav"))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)  # Play background music on loop

    while running:
        # Draw the tiled floor first
        screen.blit(floor_surface, (0, 0))
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:  # Left mouse button
                    if special_projectile_ready:  # Fire special projectile if available
                        player.shoot(mouse_pos, special=True)
                        special_projectile_ready = False  # Use up the special projectile
                        special_shoot_sound.play()
                    if use_alternate_special_projectile:  # Check if alternate special projectile is enabled
                        alt_proj = AlternateSpecialProjectiles(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                        all_sprites.add(alt_proj)
                        player.projectiles.add(alt_proj)
                        use_alternate_special_projectile = False
                        for enemy in enemies:
                            enemy.kill()  # Destroy all enemies on special projectile use
                        special_shoot_sound.play()
                    else:
                        player.shoot(mouse_pos)  # Fire normal projectile
                        shoot_sound.play()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Check for Escape key
                    running = False  # End the game

        # Get the state of keys
        keys = pygame.key.get_pressed()

        # Update sprites
        player.update(keys)  # Manually pass the keys to the player's update method
        
        for enemy in enemies:
            enemy.update()  # No need to pass keys for enemies
            
        particles.update()
        pickups.update()
        
             # Update each projectile individually based on its type
        for projectile in player.projectiles:
            if isinstance(projectile, specialProjectile):
                projectile.update(enemies)  # Only pass `enemies` to special projectiles that need it
            elif isinstance(projectile, AlternateSpecialProjectiles):
                projectile.update()  # No enemies argument needed
            else:
                projectile.update()  # Regular projectiles don't need `enemies` either

        for pickup in pygame.sprite.spritecollide(player, pickups, True):
            pickup.kill()  # Remove the pickup item from screen
            
            # Check if the pickup is purple to determine the special projectile type
            if pickup.is_purple:
                use_alternate_special_projectile = True
            else:
                use_alternate_special_projectile = False
            # Set special projectile as ready to use
            special_projectile_ready = True
        
          # Check if 5 seconds have passed to spawn more enemies
        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn_time >= 5000:  # 5000 milliseconds = 5 seconds
            # Spawn the specified number of new enemies
            for _ in range(enemies_to_spawn):
                new_enemy = Enemy()
                all_sprites.add(new_enemy)
                enemies.add(new_enemy)
            
            # Update the timer and increase the number of enemies to spawn by 5
            last_enemy_spawn_time = current_time
            enemies_to_spawn += 5  # Increase the spawn count by 5 for the next interval

            
        # Check for collisions between each projectile and enemy
        for projectile in player.projectiles:
            for enemy in enemies:
                if pygame.sprite.collide_mask(projectile, enemy):  # Pixel-perfect collision check
                    # Destroy both projectile and enemy on collision
                    projectile.kill()
                    enemy.kill()
                    kills += 1 
                    death_sound.play()  # Play death sound


                    # Optional: Add particle effect or score increment here
                    for _ in range(10):  # Example: Add particles
                        particle = Particle(
                            pos=enemy.rect.center,
                            color=(255, 0, 0),  # Red for effect
                            size=random.randint(3, 6),
                            lifespan=30
                        )
                        particles.add(particle)
                        
                    # Drop a pickup every 10 kills
                    if kills % 10 == 0:
                        pickup = PickupItem(enemy.rect.center)
                        pickups.add(pickup)
                        all_sprites.add(pickup)    
                    break  # Exit inner loop to avoid redundant checks for this projectile
         # Check for pickup collection by the player
        if pygame.sprite.spritecollideany(player, pickups):
            for pickup in pygame.sprite.spritecollide(player, pickups, True):
                special_projectile_ready = True  # Enable special projectile on pickup
                pickup.kill()  # Remove pickup item from screen
                            
        # Check for collisions between the player and enemies pixel perfect
        for enemy in enemies:
            if pygame.sprite.collide_mask(player, enemy):
                running = False  # End the game if a collision is detected
                break  # Exit the loop on collision
            
        # Calculate the elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert to seconds


        
        # Render the timer
        timer_text = font.render(f"Time Survived: {elapsed_time} seconds", True, BLACK)
        kills_text = font.render(f"Enemies Killed: {kills}", True, BLACK)
        timer_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        kills_rect = kills_text.get_rect(center=(SCREEN_WIDTH // 2, 50))  # Display kills below the timer

        
        

       

        # Draw all sprites
        all_sprites.draw(screen)
        player.projectiles.draw(screen)  # Draw projectiles separately
        particles.draw(screen)
        specialPro.draw(screen)  # Draw special projectiles
        altPro.draw(screen)  # Draw special projectiles
                
        

    

        # Draw the timer on the screen
        screen.blit(timer_text, timer_rect)
        screen.blit(kills_text, kills_rect)


        # Refresh the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Show the game over screen
    show_game_over_screen(elapsed_time, clock, kills)

