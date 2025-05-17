from flask import Flask, app, redirect, render_template
from Script import Scraper

app = Flask(__name__)


# default route
@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5555)
