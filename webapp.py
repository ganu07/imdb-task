from flask import Flask

# from helpers.db import load_db
# from helpers.parser import Parser
from views.movies import blueprint


def create_app():
    # Create DB
    # load_db()

    # parser = Parser('imdb.json')
    # parser.populate()

    # Instantiate flask app
    app = Flask(__name__)

    # Register Blueprint
    app.register_blueprint(blueprint)

    # Return app
    return app