import flask

"""flask. - anything after comes from flask library
Flask - implements application object"""

app = flask.Flask(__name__)
"""routes interpret different pages of a page"""

@app.route("/")
def index():
    #return "Hello World"
    #return flask.render_template("index.html")
    return flask.render_template("index.html", name = "jonathan")
    #putting the html in a different file helps make the python code cleaner and easier to read
app.run()

