#!/usr/bin/python3
"""
States rendering
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """
    tears-down session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_page():
    """
    render list of states
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def state_cites_page():
    """
    render list of cities
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
