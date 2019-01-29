class Deck:

    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                pass

    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        pass
