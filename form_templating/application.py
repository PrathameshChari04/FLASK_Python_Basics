from flask import Flask, render_template, request

app=Flask(__name__)
app.run()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method ==  "GET":
        return("Please Fill the Form ")
    else:
        name= request.form.get("name")
        city= request.form.get("city")
        return render_template("submit.html",name=name,city=city)

