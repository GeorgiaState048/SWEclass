import flask
from nyt import article_search
# test push
app = flask.Flask(__name__)

@app.route("/")

def index():
    """landing page"""
    headlines, snippets = article_search()
    return flask.render_template(
        "index.html",
        num_articles=len(headlines),
        headlines=headlines,
        snippets=snippets,
    )

app.run()
