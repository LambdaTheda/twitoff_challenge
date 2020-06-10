# app_dev/__init__.py

from flask import Flask

from app_dev.routes.wel_routes import wel_routes
from app_dev.routes.tweet_routes import tweet_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(wel_routes)
    app.register_blueprint(tweet_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)