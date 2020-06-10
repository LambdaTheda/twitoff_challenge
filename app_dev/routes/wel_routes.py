# app_dev/routes/home_routes.py

from flask import Blueprint

wel_routes = Blueprint("wel_routes", __name__)

@wel_routes.route("/")
def index():
    return f"Index Page"

@wel_routes.route("/welcome")
def about():
    return "Welcome to Twitoff Challenge"
