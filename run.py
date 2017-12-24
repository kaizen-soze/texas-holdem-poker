from python.objects.deck import Deck
from python.objects.playerHand import PlayerHand
from python.objects.communityCards import CommunityCards
from python.logic.rank import Rank

deck = Deck()

# https://www.wikihow.com/Shuffle-and-Deal-Texas-Holdem
# TODO: Shuffle, split deck an appropriate number of times

print("Dealing to 3 players.\n")

playerOne = PlayerHand()
playerTwo = PlayerHand()
playerThree = PlayerHand()
community = CommunityCards()
rank = Rank()

playerOne.deal(deck.nextCard())
playerTwo.deal(deck.nextCard())
playerThree.deal(deck.nextCard())

playerOne.deal(deck.nextCard())
playerTwo.deal(deck.nextCard())
playerThree.deal(deck.nextCard())

print("Flop:")

deck.burn()
community.deal(deck.nextCard())
community.deal(deck.nextCard())
community.deal(deck.nextCard())
community.showFlop()

playerOne.addCommunityCards(community.flop)
playerTwo.addCommunityCards(community.flop)
playerThree.addCommunityCards(community.flop)

print("\nTurn:")
deck.burn()
community.deal(deck.nextCard())
community.showTurn()

playerOne.addCommunityCards(community.turn)
playerTwo.addCommunityCards(community.turn)
playerThree.addCommunityCards(community.turn)

print("\nRiver:")
deck.burn()
community.deal(deck.nextCard())
community.showRiver()
playerOne.addCommunityCards(community.river)
playerTwo.addCommunityCards(community.river)
playerThree.addCommunityCards(community.river)

print("\nPlayer One Hand:")
playerOne.showHoleCards()
playerOne.handStrength = rank.calculateStrength(playerOne)

print("Player Two Hand:")
playerTwo.showHoleCards()
playerTwo.handStrength = rank.calculateStrength(playerTwo)

print("Player Three Hand:")
playerThree.showHoleCards()
playerThree.handStrength = rank.calculateStrength(playerThree)
