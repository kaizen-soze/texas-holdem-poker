from flask import Flask
from flask import jsonify

from python.objects.deck import Deck
from python.objects.playerHand import PlayerHand
from python.objects.communityCards import CommunityCards
from python.logic.rank import Rank

app = Flask(__name__)

# source $VENV_HOME/poker/bin/activate
# gunicorn --bind 0.0.0.0:5000 wsgi:app
# Run from the command line

# https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications#structuring-the-application-directory


@app.route('/')
def index():
    deck = Deck()
    deck.prepareFlop()
    
    community = CommunityCards()
    community.deal(deck.nextCard())
    community.deal(deck.nextCard())
    community.deal(deck.nextCard())
    flop = community.showFlop()
    return jsonify(flop)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
