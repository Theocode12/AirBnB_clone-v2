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


@app.route("/states", strict_slashes=False)
def states_page():
    """
    render list of states
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_cites_page(id):
    """
    render list of cities
    """
    state = None
    for _state in storage.all(State).values():
        if _state.id == id:
            state = _state
            break
    return render_template("9-states.html", state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
