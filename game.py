import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen

    def update(self):
        # TODO: Update game logic here
        pass

    def draw(self):
        # TODO: Draw the board here
        # This is where you'll draw the hexagonal grid based on the README
        self.screen.fill((0, 0, 0))  # Clear the screen with a black background

        # Example of drawing a single hexagon
        pygame.draw.polygon(self.screen, (255, 255, 255), self.get_hexagon_points(100, 100, 30))

    def get_hexagon_points(self, x, y, size):
        """Calculate the points of a hexagon centered at (x, y) with the given size."""
        points = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = pygame.math.radians(angle_deg)
            points.append((x + size * pygame.math.cos(angle_rad),
                           y + size * pygame.math.sin(angle_rad)))
        return points
