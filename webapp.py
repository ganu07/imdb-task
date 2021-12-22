from flask import Flask


from views.movies import blueprint


def create_app():

    # Instantiate flask app
    app = Flask(__name__)
	app.run(debug=True, port=0.0.0.0)

    # Return app
    return app
