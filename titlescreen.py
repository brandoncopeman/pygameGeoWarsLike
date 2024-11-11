import pygame
from settings import *

pygame.font.init()
title_font = pygame.font.Font(None, 80)  # Large font for the title
button_font = pygame.font.Font(None, 80)  # Regular font for buttons

def render_text_with_shadow(text, font, text_color, shadow_color, shadow_offset=(2, 2)):
    """Render text with a shadow effect."""
    shadow_text = font.render(text, True, shadow_color)
    base_text = font.render(text, True, text_color)
    return shadow_text, base_text, shadow_offset

def show_title_screen():
    
    # Load background image for title screen (optional)
    title_background = pygame.image.load("assets/ts1.png").convert()
    title_background = pygame.transform.scale(title_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and play title screen music
    pygame.mixer.music.load("assets/sounds/titlemusic.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Loop indefinitely

    # Define "Play" button
    play_button_text = font.render("Play", True, WHITE)
    play_button_rect = play_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Define "quit" button
    quit_text = font.render("Quit", True, WHITE)
    quit_rect = play_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))


    # Title screen loop
    showing_title = True
    while showing_title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    showing_title = False  # Exit title screen to start the game
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    showing_title = False  # Exit title screen to start the game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        # Draw title background
        screen.blit(title_background, (0, 0))

        # Render title text with shadow effect
        shadow_text, title_text, shadow_offset = render_text_with_shadow("Little Alien Survivor", title_font, WHITE, BLACK, (3, 3))
        title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        shadow_text_rect = title_text_rect.move(shadow_offset)

        # Draw shadow and then main title text on top
        screen.blit(shadow_text, shadow_text_rect)
        screen.blit(title_text, title_text_rect)
        
        # Draw the "Play" button
        pygame.draw.rect(screen, BLACK, play_button_rect.inflate(20, 20))  # Black rectangle background for button
        screen.blit(play_button_text, play_button_rect)  # White text on top of button
        
        # Draw the "quit" button
        pygame.draw.rect(screen, BLACK, quit_rect.inflate(20, 20))  # Black rectangle background for button
        screen.blit(quit_text, quit_rect)  # White text on top of button

        # Update display
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
        
    pygame.mixer.music.stop()