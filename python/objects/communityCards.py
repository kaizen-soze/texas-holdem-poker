from python.objects.card import Card
from python.objects.hand import Hand


class CommunityCards(Hand):
    """Represents the cards belonging to all players"""

    def __init__(self):
        self.hand = []
        pass

    def deal(self, card):
        """Add a Card object to the hand"""
        self.hand.append(card)

        size = len(self.hand)
        hand = self.hand

        if size == 3:
            self.flop = [hand[0], hand[1], hand[2]]
        elif size == 4:
            self.turn = [hand[3]]
        elif size == 5:
            self.river = [hand[4]]

    def describeLastCard(self, card):
        print(card)

    def showFlop(self):
        """Prints the cards in the Flop to the screen."""
        # We only need to print individual card objects,
        # so there's no need to set up a loop
        return [self.hand[0], self.hand[1], self.hand[2]]

    def showTurn(self):
        """Prints the Turn card to the screen."""
        print(self.hand[3])

    def showRiver(self):
        """Prints the River card to the screen."""
        print(self.hand[4])
