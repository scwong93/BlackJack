import random

suits = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King':10}

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips. You have: {}'.format(chips.total))
            else:
                break


def hit(deck, hand):
    pass


def hit_or_stand(deck, hand):
    global playing

    pass


def show_some(player,dealer):
    pass


def show_all(player,dealer):
    pass


def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


def push():
    pass
