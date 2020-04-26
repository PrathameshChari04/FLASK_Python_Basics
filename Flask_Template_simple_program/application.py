from flask import Flask, render_template


app = Flask(__name__)
app.run()


@app.route('/')
def index():
    name = "Bruce Wayne"
    return render_template("index.html", name=name)


@app.route('/bye')
def bye():
    name = "Listen"
    return render_template("index.html", name=name)


