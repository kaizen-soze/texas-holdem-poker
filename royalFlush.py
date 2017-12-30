from python.objects.card import Card
from python.objects.deck import Deck
from python.objects.playerHand import PlayerHand
from python.objects.communityCards import CommunityCards
from python.logic.rank import Rank

deck = Deck()

# https://www.wikihow.com/Shuffle-and-Deal-Texas-Holdem
# TODO: Shuffle, split deck an appropriate number of times

print("Dealing to 3 players.\n")

playerOne = PlayerHand()
community = CommunityCards()
rank = Rank()

suit = 'D'
ace = Card('A', suit)
king = Card('K', suit)
queen = Card('Q', suit)
jack = Card('J', suit)
ten = Card('10', suit)

playerOne.deal(ace)
playerOne.deal(king)

print("Flop:")

deck.burn()
community.deal(queen)
community.deal(jack)
community.deal(ten)
community.showFlop()

playerOne.addCommunityCards(community.flop)

print("\nTurn:")
deck.burn()
community.deal(deck.nextCard())
community.showTurn()

playerOne.addCommunityCards(community.turn)

print("\nRiver:")
deck.burn()
community.deal(deck.nextCard())
community.showRiver()
playerOne.addCommunityCards(community.river)

print("\nPlayer One Hand:")
playerOne.showHoleCards()
playerOne.handStrength = rank.calculateStrength(playerOne)

#print("Clubs: {0} | Diamonds: {1} | Hearts: {2} | Spades: {3}".format(self.clubs, self.diamonds, self.hearts, self.spades))

