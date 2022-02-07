import flask

fav_shows = ["Stranger Things", "All of us Are Dead", "You", "Narcos", "Russian Doll"]
images = ["/static/StrangerThings.jpg", "/static/AllOfUsAreDead.jpg", "/static/You.jpg", "/static/Narcos.jpg", "/static/RussianDoll.jpg"]
"""flask. - anything after comes from flask library
Flask - implements application object"""

app = flask.Flask(__name__)
"""routes interpret different pages of a page"""

@app.route("/")
def index():
    return flask.render_template("index.html", len = len(fav_shows), fav_shows = fav_shows, priority = 2, len1 = len(images), images = images)
    #return "Hello World"
app.run()
