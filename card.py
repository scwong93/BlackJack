class Card:

    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

    def __str__(self):
        return self.card + " of " + self.suit
