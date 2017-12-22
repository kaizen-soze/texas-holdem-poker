import random
from python.objects.card import Card

class Hand:
    'A set of cards'

    def __init__(self):
        self.hand = []
        pass

    def deal(self, card):
        self.hand.append(card)

    def __str__(self):
        thisHand = '';
        for card in self.hand:
            thisHand += str(card) + "\n"

        return thisHand