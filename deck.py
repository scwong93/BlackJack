class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for card in cards:
                self.deck.append(Card(suit,card))

    def __str__(self):
        deck_comp = ''
        for i in self.deck:
            deck.comp += '\n' + i.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
