import random
from deck import Deck
from card import Card
from hand import Hand
from chips import Chips

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


while True:
    print('Welcome to the game of BlackJack!')


    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips

    player_chips = Chips()

    # Prompt the Player for their bet

    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)

    show_some(player_hand,dealer_hand)


    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)


        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)


        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total
    print('Your current chips total is {}'.format(player_chips.total))

    # Ask to play again
    new_game = input('Would you like to play another round? [Y/N]: ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break
