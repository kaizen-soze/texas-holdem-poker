import random
from python.objects.card import Card
from python.objects.hand import Hand

class PlayerHand(Hand):
    'A set of two cards'

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