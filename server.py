from flask import Flask, request
from random import choice, randint


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""

    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    """Say hello"""

    return """<html>
                <body>
                    <h1>
                    Hi Everybody!
                    </h1>
                </body>
            </html>"""

@app.route('/lucky')
def lucky_number():
    """Provides a random lucky number"""
    # add code here of getting a lucky number and return a string
    # with the lucky number
    lucky_num = randint(1, 100)
    lucky_message = "Your lucky number is %s" % lucky_num
    return "<html><body><h1>" + lucky_message + "</h1></body></html>"

@app.route('/dog')
def look_at_dog():
    picture = "<img src='http://pbs.twimg.com/media/CkXsQjNWEAAJVua.jpg:large'>"
    return '<html><body><h1>Would you like to look at a dog?</h1><img src="http://pbs.twimg.com/media/CkXsQjNWEAAJVua.jpg:large"></body></html>'


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
