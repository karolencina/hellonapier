from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello Napier</h2><h3>What\'s up?</h3>'
