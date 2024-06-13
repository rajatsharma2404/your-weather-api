from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    return "Hello"

app.run(debug=True)