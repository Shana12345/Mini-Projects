#!/usr/bin/env python3.8
# you want to get to 21
# what do you need? nums from 2-10, then ACE JACK QUEEN  KING
# how many players?
#
def blackjack():
    # defining all cards
    card_deck = 'Ace,2,3,4,5,6,7,8,9,10'.split
    card_suits = 'Spades, Hearts, Diamonds, Clubs'.split

    


def blackjack2(card):
    rest = '2,3,4,5,6,7,8,9'.split
    royals = 'J, Q, K, 1'.split

    if card[:1] in royals:
        return int(10)
    elif card[1:2] in rest:
        return int(card[:1])
    
    elif card[:1]