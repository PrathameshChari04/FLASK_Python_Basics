from flask import Flask, render_template, request

app=Flask(__name__)
app.run()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name= request.form.get("name")
    return render_template("submit.html",name=name)

