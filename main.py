import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Boardstone Battlefields')

# Create the game object
game = Game(screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic and draw the board
    game.update()
    game.draw()

    # Update the display
    pygame.display.flip()

# Clean up Pygame
pygame.quit()
