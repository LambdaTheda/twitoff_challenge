from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page.'

@app.route('/tweets')
def tweet():
    return 'Motivation is ever fleeting'