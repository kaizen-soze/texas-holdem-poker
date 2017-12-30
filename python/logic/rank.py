import random
from python.objects.card import Card
from python.objects.playerHand import PlayerHand


class Rank():
    'Logic relating to the ranking of poker hands'

    def __init__(self):
        pass

    def calculateStrength(self, hand: PlayerHand):
        """Calculates the strength of the current hand. Returns a dictionary"""

        if self.isRoyalFlush(hand):
            return {'score': 108, 'name': 'Royal Flush'}
        elif self.isStraightFlush(hand):
            return {'score': 96, 'name': 'Straight Flush'}
        elif self.isFourOfAKind(hand):
            return {'score': 84, 'name': 'Four Of A Kind'}
        elif self.isFullHouse(hand):
            return {'score': 72, 'name': 'Full House'}
        elif self.isFlush(hand):
            return {'score': 60, 'name': 'Flush'}
        elif self.isStraight(hand):
            return {'score': 48, 'name': 'Straight'}
        elif self.isThreeOfAKind(hand):
            return {'score': 36, 'name': 'Three Of A Kind'}
        elif self.isTwoOfAKind(hand):
            return {'score': 24, 'name': 'Pair'}
        else:
            return {'score': 0, 'name': 'High Card'}
        
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
        return player.hasStraightFlush

    def isFourOfAKind(self, player: PlayerHand):
        return self.__xOfAKind(4, player)

    def isFullHouse(self, player: PlayerHand):
        hand = player.sortedHand
        cardValues = []
        for card in hand:
            cardValues.append(card.value)

        appearsThreeTimes = False
        appearsTwoTimes = False

        # These are unique values that are being counted,
        # so it's impossible for the variables above to
        # reference the same value
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
        return player.hasFlush

    def isStraight(self, player: PlayerHand):
        return player.hasStraight

    def isThreeOfAKind(self, player: PlayerHand):
        return self.__xOfAKind(3, player)

    def isTwoOfAKind(self, player: PlayerHand):
        return self.__xOfAKind(2, player)

    def __xOfAKind(self, x: int, player: PlayerHand):
        """Returns true if the hand has x cards with the same value"""
        hand = player.sortedHand
        cardValues = []
        for card in hand:
            cardValues.append(card.value)

        for value in cardValues:
            count = cardValues.count(value)

            if count == x:
                return True

        return False
