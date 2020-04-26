from flask import Flask, render_template


app = Flask(__name__)
app.run()

@app.route('/')
def index():
    names = ["Bruce","Tony","Logan","Steve"]
    return render_template("index.html",names=names)
