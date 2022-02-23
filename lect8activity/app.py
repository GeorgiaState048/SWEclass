import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pnjonadutwpcns:68c0e33ca6cea3a2c70487bf5694f03e185232d4636ce2c57844651ca3b180ce@ec2-44-192-245-97.compute-1.amazonaws.com:5432/ddggelsgi946kc"
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues
from models import Person

@app.route('/')
def index():
    """landing page"""
    return "Hello, world!"

if __name__ == "__main__":
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
    )
   