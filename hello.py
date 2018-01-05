from flask import Flask
app = Flask(__name__)

# gunicorn --bind 0.0.0.0:5000 wsgi:app
# Run from the command line


@app.route('/')
def index():
    return '<h1>Hello, Texas Holdem Poker!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
