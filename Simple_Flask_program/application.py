from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey You there , you people are just awsome'

@app.route('/bruce')
def bruce():
    return 'Hey this bruce wayn'

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name} !"