import random
from python.objects.card import Card
from python.objects.playerHand import PlayerHand


class Rank():
    'Logic relating to the ranking of poker hands'

    def __init__(self):
        pass

    def calculateStrength(self, hand: PlayerHand):
        """Calculates the strength of the current hand."""

        if self.isRoyalFlush(hand):
            return 108
        elif self.isStraightFlush(hand):
            return 96
        elif self.isFourOfAKind(hand):
            return 84
        elif self.isFullHouse(hand):
            return 72
        elif self.isFlush(hand):
            return 60
        elif self.isStraight(hand):
            return 48
        elif self.isThreeOfAKind(hand):
            return 36
        elif self.isTwoOfAKind(hand):
            return 24
        else:
            return 0
        
    def isRoyalFlush(self, player: PlayerHand):
        """Returns true if the hand has A K Q J 10 suited"""
        suit = player.hand[0].suit
        if (
            player.hasFlush and
            player.hand[0].value == 'A' and
            player.hand[1].value == 'K' and
            player.hand[2].value == 'Q' and
            player.hand[3].value == 'J' and
            player.hand[4].value == '10' and
            player.hand[1].suit == suit and
            player.hand[2].suit == suit and
            player.hand[3].suit == suit and
            player.hand[4].suit == suit
        ):
            return True
        else:
            return False

    def isStraightFlush(self, player: PlayerHand):
        """Returns true if the hand has a sequence of 5 cards suited"""
        return player.hasStraightFlush

    def isFourOfAKind(self, player: PlayerHand):
        hand = player.sortedHand
        cardValues = []
        for card in hand:
            cardValues.append(card.value)

        for value in cardValues:
            count = cardValues.count(value)

            if count == 4:
                return True

        return False

    def isFullHouse(self, player: PlayerHand):
        hand = player.sortedHand
        cardValues = []
        for card in hand:
            cardValues.append(card.value)

        appearsThreeTimes = False
        appearsTwoTimes = False
        for value in cardValues:
            count = cardValues.count(value)

            if count == 3:
                appearsThreeTimes = True
            elif count == 2:
                appearsTwoTimes = True

        if appearsThreeTimes is True and appearsTwoTimes is True:
            return True
        else:
            return False

    def isFlush(self, player: PlayerHand):
        """Returns true if the hand has a sequence of 5 cards"""
        return player.hasFlush

    def isStraight(self, player: PlayerHand):
        """Returns true if the hand has a sequence of 5 cards"""
        return player.hasStraight

    def isThreeOfAKind(self, player: PlayerHand):
        """Returns true if the hand has a sequence of 5 cards"""
        hand = player.sortedHand
        cardValues = []
        for card in hand:
            cardValues.append(card.value)

        for value in cardValues:
            count = cardValues.count(value)

            if count == 3:
                return True

        return False

    def isTwoOfAKind(self, player: PlayerHand):
        """Returns true if the hand has a sequence of 5 cards"""
        hand = player.sortedHand
        cardValues = []
        for card in hand:
            cardValues.append(card.value)

        for value in cardValues:
            count = cardValues.count(value)

            if count == 2:
                return True

        return False
