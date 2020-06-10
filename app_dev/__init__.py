# app_dev/__init__.py

from flask import Flask

from app_dev.routes.wel_routes import wel_routes
#from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(wel_routes)
    #app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)