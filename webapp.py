from flask import Flask


from views.movies import blueprint


def create_app():

    # Instantiate flask app
    app = Flask(__name__)
	app.run()

    # Return app
    return app
