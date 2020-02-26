#!/usr/bin/env python3.8

#list = 'iloveprogramming'
#print(list[0:1])
#class Game:
   # def __init__(self, round1, round2):
       # self.first = round1
       # self.second = round2

#royals = 'J, Q, K, 1'.split

#if card[:1] in royals:
    #return int(10)


from random import randint

class Card:
    def __init__(self):
        pass

    def card_value(self):
        pass

    card_face = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_suit = ['Hearts','Spades','Clubs','Diamonds']



class Deck(Card):
    new_deck = []
    length = len(new_deck) #testing purposes

    for i in Card.card_suit:
        for j in Card.card_face:
            new_deck.append(j + ' of ' + i)

    def new_card(self):
        #instead of return, use yield?
        return (self.new_deck[randint(0,len(self.new_deck)-1)])
    def remove_card(self,card):
        self.new_deck.remove(card)



deck1 = Deck()
card1 = deck1.new_card()
deck1.remove_card(card1)
card2 = deck1.new_card()
deck1.remove_card(card2)
print(str(card1) + " and " + str(card2))
print(len(deck1.new_deck))