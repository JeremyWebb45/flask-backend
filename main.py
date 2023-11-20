import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("about.html", testData={'startState': (0,0), 'goalState': (0,0)})

@app.route("/data-science")
def dataScience():
    return render_template("data-science.html")

@app.route("/front-end")
def frontEnd():
    return render_template("front-end.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)