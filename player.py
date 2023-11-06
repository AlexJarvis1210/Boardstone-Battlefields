class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.mana = 0
        self.deck = []  # This will be a list of card objects
        self.hand = []  # This will be a list of card objects

    def shuffle_deck(self):
        # Shuffle the deck
        import random
        random.shuffle(self.deck)

    def draw_card(self):
        # Draw a card from the deck into the hand
        if self.deck:
            self.hand.append(self.deck.pop(0))
            
    def gain_mana(self, amount):
        # Increase player's mana
        self.mana += amount

    def use_mana(self, cost):
        # Use player's mana for card play or abilities
        if self.mana >= cost:
            self.mana -= cost
            return True
        return False

    def modify_health(self, amount):
        # Modify player's health for damage or healing
        self.health += amount
        if self.health > 30:
            self.health = 30
        elif self.health < 0:
            self.health = 0

    def play_card(self, card, x, y):
        # Play a card from the hand to the board
        if card in self.hand:
            self.hand.remove(card)
            self.grid[y][x] = card  # Assuming top-left is (0,0) and x is horizontal
    # Draw a card from the deck into the hand
        if self.deck:
            self.hand.append(self.deck.pop(0))
