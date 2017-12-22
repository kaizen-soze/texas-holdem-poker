from python.objects.deck import Deck
from python.objects.playerHand import PlayerHand

deck = Deck()

print(deck)
deck.burn()
print("Burned one card")
print("Dealing to 3 players.")

playerOne = PlayerHand()
playerTwo = PlayerHand()
playerThree = PlayerHand()

playerOne.deal(deck.nextCard())
playerTwo.deal(deck.nextCard())
playerThree.deal(deck.nextCard())

playerOne.deal(deck.nextCard())
playerTwo.deal(deck.nextCard())
playerThree.deal(deck.nextCard())

print("Player One Hand:")
print(playerOne)

print("Player Two Hand:")
print(playerTwo)

print("Player Three Hand:")
print(playerThree)

