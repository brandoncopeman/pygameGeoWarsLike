import pygame
from settings import *
from game import *

pygame.init()

# Main loop to start and restart the game
def main():
    while True:
        start_game()  # Run the game, restart after game over

        # After a game over, wait for the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Exit the program

# Start the game
main()

# Quit pygame (this will only be reached if the player exits)
pygame.quit()