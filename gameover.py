import pygame
from settings import *

def show_game_over_screen(score, clock):
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

        # Render the game over screen
        screen.fill(WHITE)
        game_over_text = font.render("Game Over", True, BLACK)
        score_text = font.render(f"Time Survived: {score} seconds", True, BLACK)
        play_again_text = font.render("Press Enter to Play Again", True, BLACK)
        quit_text = font.render("Press Escape to Quit", True, BLACK)

        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(play_again_text, play_again_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        clock.tick(FPS)
