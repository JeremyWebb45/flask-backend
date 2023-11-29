import datetime

from flask import Flask, render_template, request

from server import PathPlanning

pathPlanningController = PathPlanning.PathPlanningController()

app = Flask(__name__)


@app.route("/")
def root():
    grid = pathPlanningController.getGrid()
    height = pathPlanningController.getHeight()
    width = pathPlanningController.getWidth()
    return render_template("about.html", grid=grid, height=height, width=width)

@app.route("/api/path-planning", methods=['GET', 'POST'])
def pathPlanning():
    print(request.args.get('body'))
    return {'message': 'hey'}

@app.route("/data-science")
def dataScience():
    return render_template("data-science.html")

@app.route("/front-end")
def frontEnd():
    return render_template("front-end.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)