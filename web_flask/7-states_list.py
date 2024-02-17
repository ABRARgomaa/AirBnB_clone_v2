#!/usr/bin/python3
"""
 Hello Flask!
"""
from flask import Flask, render_template
from models import storage
import json
from models import State, City

web_app = Flask(__name__)


@web_app.teardown_appcontext
def close_storage(error):
    storage.close()


@web_app.route("/states_list", strict_slashes=False)
def states_list():
    """
    display a HTML page
    """
    return render_template('7-states_list.html')


if __name__ == "__main__":
    web_app.run(host='0.0.0.0', port=5000)
