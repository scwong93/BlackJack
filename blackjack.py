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
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter H or S: ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn.")
            playing = False
        else:
            print('Sorry, I did not understand that. Please enter H or S.')
            continue
        break


def show_some(player,dealer):
    print("Dealer's Hand: ")
    print('One card hidden')
    print(dealer.cards[1])
    print('\n')
    print("Player's Hand: ")
    for card in player.cards:
        print(card)


def show_all(player,dealer):
    print("Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player's Hand: ")
    for card in player.cards:
        print(card)


def player_busts(player, dealer, chips):
    print('Player busted!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Dealer busted!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.lose_bet()


def push(player, dealer):
    print('Player and Dealer tied. PUSH!')
