class Board:
        
    def draw(self, screen):
        # This method will use Pygame to draw the board on the screen
        # Placeholder for drawing code
        pass
    def __init__(self, width, height):
        # Initialize the board with empty hexes
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.special_tiles = {}  # Dictionary to store special tiles and their effects

    def display_board(self):
        # Display the board state
        for row in self.grid:
            print(' '.join(['.' if cell is None else 'X' for cell in row]))
            
    def is_tile_occupied(self, x, y):
        # Check if a tile is occupied
        return self.grid[y][x] is not None

    def remove_card_from_board(self, x, y):
        # Remove a card from the board
        if self.is_tile_occupied(x, y):
            self.grid[y][x] = None

    def set_special_tile(self, x, y, effect):
        # Set a special tile at the given coordinates with the specified effect
        self.special_tiles[(x, y)] = effect

    def get_tile_effect(self, x, y):
        # Get the effect of the tile at the given coordinates
        return self.special_tiles.get((x, y), None)
        # Display the board state
        for row in self.grid: # There's an issue here Gee!
            print(' '.join(['.' if cell is None else 'X' for cell in row])) 
