from python.objects.deck import Deck
from python.objects.playerHand import PlayerHand
from python.objects.communityCards import CommunityCards
from python.logic.rank import Rank

deck = Deck()
deck.prepareFlop()

# https://www.wikihow.com/Shuffle-and-Deal-Texas-Holdem
# TODO: Shuffle, split deck an appropriate number of times

print("Dealing to 3 players.\n")

playerOne = PlayerHand('Player One')
playerTwo = PlayerHand('Player Two')
playerThree = PlayerHand('Player Three')
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
playerOne.results = rank.calculateStrength(playerOne)
print("Strength: {0}".format(playerOne.results['score']))

print("Player Two Hand:\n")
playerTwo.showHoleCards()
playerTwo.results = rank.calculateStrength(playerTwo)
print("Strength: {0}".format(playerTwo.results['score']))

print("Player Three Hand:\n")
playerThree.showHoleCards()
playerThree.results = rank.calculateStrength(playerThree)
print("Strength: {0}".format(playerThree.results['score']))

players = (playerOne, playerTwo, playerThree)

highestHand = 0
highestScore = 0
winningPlayer = None
tie = []

for player in players:
    # Calculate the score for their hand
    player.calculateScore()

    if player.results['score'] > highestHand:
        highestHand = player.results['score']
        winningPlayer = player
        del tie[:]
    elif (player.results['score'] == highestHand
          and player.individualScore > highestScore):
            highestScore = player.individualScore
            winningPlayer = player
            del tie[:]
    elif (player.results['score'] == highestHand
          and player.individualScore == highestScore):
        tie.append(winningPlayer)
        tie.append(player)

if len(tie) == 0:
    print("The winning player is {0} with a {1}"
          .format(winningPlayer.name, winningPlayer.results['name']))
else:
    for player in tie:
        print("We have a tie!")
        print("{0} had a {1}".format(player.name, player.results['name']))
