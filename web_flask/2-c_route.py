#!/usr/bin/python3
"""
Flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    root directory
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb directory
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_life(text):
    """
    text substitution
    """
    return "C {}".format(text).replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
