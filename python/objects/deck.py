import random
from collections import deque
from python.objects.card import Card

class Deck:
    'A representation of a deck of cards'

    def __init__(self):
        self.__createCards()
        pass

    def burn(self):
        self.deck.popleft()

    def nextCard(self):
        return self.deck.popleft()

    def __createCards(self):
        values = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
        suits = ('H', 'S', 'D', 'C')

        deck = deque()

        for suit in suits:
            for value in values:
                deck.append(Card(value, suit))

        random.shuffle(deck)

        self.deck = deck

    def __str__(self):
        completeDeck = '';
        for card in self.deck:
            completeDeck += str(card) + "\n"

        return completeDeck