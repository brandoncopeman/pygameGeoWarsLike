import pygame
from settings import screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from  titlescreen import show_title_screen

def render_text_with_shadow(text, font, text_color, shadow_color, shadow_offset=(2, 2)):
    """Render text with a shadow effect."""
    shadow_text = font.render(text, True, shadow_color)
    base_text = font.render(text, True, text_color)
    return shadow_text, base_text, shadow_offset

def show_instructions_screen():
    background_image = pygame.image.load("assets/instructions.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    instructions = [
        "Instructions:",
        "- Use WASD or arrow keys to move your character.",
        "- Use the mouse to aim and left-click to shoot.",
        "- Survive as long as you can against incoming enemies!",
        "- Press ESC anytime to quit the game.",
        "",
        "Press ENTER to start the game."
    ]
    # Calculate total height of instructions to center them vertically
    line_height = 40  # Vertical space per line, including spacing
    total_height = len(instructions) * line_height
    start_y = (SCREEN_HEIGHT - total_height) // 2  # Center the block of text vertically

    showing_instructions = True
    while showing_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to continue
                    showing_instructions = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

         #draw bg image
        screen.blit(background_image, (0, 0))
    # Main loop for the instructions screen

        # Render each line of instructions with shadow effect
        for i, line in enumerate(instructions):
            shadow_text, base_text, shadow_offset = render_text_with_shadow(line, font, WHITE, BLACK, (2, 2))
            text_rect = base_text.get_rect(center=(SCREEN_WIDTH // 2,start_y + i * line_height))
            shadow_rect = text_rect.move(shadow_offset)

            # Draw shadow and then main text on top
            screen.blit(shadow_text, shadow_rect)
            screen.blit(base_text, text_rect)

        # Update display
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        
    pygame.mixer.music.stop()