import random
from python.objects.card import Card
from python.objects.hand import Hand

class CommunityCards(Hand):
    'A set of three cards'

    def __init__(self):
        self.hand = []
        pass

    def deal(self, card):
        self.hand.append(card)

        hand = self.hand
        size = len(hand)

        if size == 3:
            self.flop = [hand[0], hand[1], hand[2]]
        elif size == 4:
            self.turn = [hand[3]]
        elif size == 5:
            self.river = [hand[4]]

    def describeLastCard(self, card):
        print(card)

    def showFlop(self):
        print(self.hand[0]);
        print(self.hand[1]);
        print(self.hand[2])

    def showTurn(self):
        print(self.hand[3])

    def showRiver(self):
        print(self.hand[4])
