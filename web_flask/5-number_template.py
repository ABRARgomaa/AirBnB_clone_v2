#!/usr/bin/python3
"""
 Hello Flask!
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def homepage():
    """
    starts a Flask web application
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    display “C ” followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    display “Python ”, followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
