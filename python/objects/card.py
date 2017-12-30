class Card:
    'A representation of a playing card'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.suitEmoji = self.__fetchEmoji(suit)
        self.score = self.__calculateScore()

    # Calculate the score of a card
    def __calculateScore(self):
        score = 0

        if self.value == 'A':
            score = 14
        elif self.value == 'K':
            score = 13
        elif self.value == 'Q':
            score = 12
        elif self.value == 'J':
            score = 11
        elif self.value == '10':
            score = 10
        elif self.value == '9':
            score = 9
        elif self.value == '8':
            score = 8
        elif self.value == '7':
            score = 7
        elif self.value == '6':
            score = 6
        elif self.value == '5':
            score = 5
        elif self.value == '4':
            score = 4
        elif self.value == '3':
            score = 3
        elif self.value == '2':
            score = 2

        return score

    def __repr__(self):
        return repr((self.value, self.suit, self.score))

    def __str__(self):
        return "%s %s" % (self.value, self.suitEmoji)

    def __fetchEmoji(self, suit):
        if suit == 'H':
            return '♥'
        elif suit == 'S':
            return '♠'
        elif suit == 'C':
            return '♣'
        elif suit == 'D':
            return '♦'
        else:
            return '?'
