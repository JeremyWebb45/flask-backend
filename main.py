import datetime

from flask import Flask, render_template

from server import PathPlanning

pathPlanningController = PathPlanning.PathPlanningController()

app = Flask(__name__)


@app.route("/")
def root():
    initData = pathPlanningController.getInfo()
    return render_template("about.html", gridData=initData)

@app.route("/data-science")
def dataScience():
    return render_template("data-science.html")

@app.route("/front-end")
def frontEnd():
    return render_template("front-end.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)