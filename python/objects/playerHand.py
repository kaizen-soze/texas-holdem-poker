from python.logic.straight import Straight
from python.objects.card import Card
from python.objects.hand import Hand


class PlayerHand(Hand):
    """A representation of the player's hand"""

    def __init__(self):
        self.hand = []
        self.sortedHand = []
        self.hole = []
        self.community = []
        self.individualScore = 0
        self.handStrength = 0
        self.handName = ''
        self.clubs = 0
        self.diamonds = 0
        self.hearts = 0
        self.spades = 0
        self.hasFlush = False
        self.hasStraight = False
        self.hasStraightFlush = False
        pass

    def deal(self, card):
        self.hand.append(card)
        self.hole.append(card)
        self.__incrementSuit(card)
        self.__sortHand()

    def showHoleCards(self):
        for card in self.hole:
            print(card)

    def addCommunityCards(self, cards: list):
        for card in cards:
            self.hand.append(card)
            self.community.append(card)
            self.__incrementSuit(card)

        self.__sortHand()
        self.__checkForStraight()

    def __incrementSuit(self, card):
        if card.suit == 'C':
            self.clubs += 1
        elif card.suit == 'D':
            self.diamonds += 1
        elif card.suit == 'H':
            self.hearts += 1
        elif card.suit == 'S':
            self.spades += 1

        self.__checkForFlush()

    def __checkForFlush(self):
        if (
            self.clubs == 5 or
            self.diamonds == 5 or
            self.hearts == 5 or
            self.spades == 5
        ):
            self.hasFlush = True

    def __sortHand(self):
        """Sorts the cards based on the score attribute."""
        self.sortedHand = sorted(
            self.hand,
            key=lambda card: card.score,
            reverse=True
        )

    def __checkForStraight(self):
        """Checks the current hand for a straight."""
        cardSequences = []
        if len(self.sortedHand) >= 5:
            cardSeq1 = self.sortedHand[:5]
            cardSeq2 = []
            cardSeq3 = []
            cardSequences.append(cardSeq1)

            if len(self.sortedHand) == 6:
                cardSeq2 = self.sortedHand[1:6]
                cardSequences.append(cardSeq2)

            if len(self.sortedHand) == 7:
                cardSeq3 = self.sortedHand[2:7]
                cardSequences.append(cardSeq3)

            # The cardSeqX objects are lists of Card objects, but
            # the sequences from straight.sequence are lists of
            # strings. We need to convert our card objects to lists
            # of strings in order to do the appropriate comparison
            seq1 = []
            seq2 = []
            seq3 = []

            for card in cardSeq1:
                seq1.append(str(card.value))

            for card in cardSeq2:
                seq2.append(str(card.value))

            for card in cardSeq3:
                seq3.append(str(card.value))

            playerSequences = [seq1, seq2, seq3]

            straight = Straight()
            handIndex = 0
            for sequence in straight.sequences:
                for hand in playerSequences:
                    if hand == sequence:
                        self.hasStraight = True
                        # check this sequence for the presence of a flush
                        if handIndex < len(cardSequences):
                            tempSeq = cardSequences[handIndex]
                            suit = tempSeq[0].suit
                            sameSuit = True
                            for card in tempSeq:
                                if card.suit != suit:
                                    sameSuit = False

                            if sameSuit is True:
                                self.hasStraightFlush = True
                        return
                        handIndex += 1
