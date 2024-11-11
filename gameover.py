import pygame
from settings import *

def render_text_with_shadow(text, font, text_color, shadow_color, shadow_offset=(2, 2)):
    """Render text with a shadow effect."""
    shadow_text = font.render(text, True, shadow_color)
    base_text = font.render(text, True, text_color)
    return shadow_text, base_text, shadow_offset

def show_game_over_screen(score, clock, kills):
        # Load the background image
    background_image = pygame.image.load("assets/bg1.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to play again
                    game_over = False
                if event.key == pygame.K_ESCAPE:  # Press Escape to quit
                    pygame.quit()
                    exit()
        #draw bg image
        screen.blit(background_image, (0, 0))
        
        # Render text with shadow for each text element
        shadow_offset = (3, 3)  # Offset for shadow effect

        game_over_shadow, game_over_text, offset = render_text_with_shadow("Game Over", font, WHITE, BLACK, shadow_offset)
        score_shadow, score_text, _ = render_text_with_shadow(f"Time Survived: {score} seconds", font, WHITE, BLACK, shadow_offset)
        kill_shadow, kill_text, _ = render_text_with_shadow(f"You Killed: {kills} Enemies", font, WHITE, BLACK, shadow_offset)
        play_again_shadow, play_again_text, _ = render_text_with_shadow("Press Enter to Play Again", font, WHITE, BLACK, shadow_offset)
        quit_shadow, quit_text, _ = render_text_with_shadow("Press Escape to Quit", font, WHITE, BLACK, shadow_offset)

        # Define text positions
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        kill_rect = kill_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))

         # Draw each text element with its shadow
        screen.blit(game_over_shadow, game_over_rect.move(offset))
        screen.blit(game_over_text, game_over_rect)

        screen.blit(score_shadow, score_rect.move(offset))
        screen.blit(score_text, score_rect)

        screen.blit(kill_shadow, kill_rect.move(offset))
        screen.blit(kill_text, kill_rect)

        screen.blit(play_again_shadow, play_again_rect.move(offset))
        screen.blit(play_again_text, play_again_rect)

        screen.blit(quit_shadow, quit_rect.move(offset))
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        clock.tick(FPS)
        
