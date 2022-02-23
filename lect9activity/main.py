import os
import flask

app = flask.Flask(__name__)
app.secret_key = "I am a secret key"

@app.route("/")
def index():
    """landing page"""
    return flask.render_template("index.html")

@app.route("/handle_form", methods=["POST"])
def handle_form():
    """handle page"""
    data = flask.request.form
    campus_id = data.get("CampusID")
    if campus_id == "jlaurent4":
        return flask.redirect(flask.url_for("welcome")) # inside the quotations are function names
    else:
        flask.flash("Wrong campus id entered")
        return flask.redirect(flask.url_for("index")) # inside the quotations is a function name
@app.route("/welcome_page")
def welcome():
    """Welcome Page"""
    return "<h1>Welcome Jonathan</h1>"

app.run()