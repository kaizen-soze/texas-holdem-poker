class Card:
    'A representation of a playing card'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.suitEmoji = self.__fetchEmoji(suit)

    def __str__(self):
        return 'Card: %s %s' % (self.value, self.suitEmoji)

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
