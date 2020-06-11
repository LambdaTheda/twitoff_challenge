# app_dev/routes/tweet_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    tweets = [
        {"id": 1, "cory_ken": "Motivate"},
        {"id": 2, "kyle_jen": "New Makeup"}
    ]
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_from_twitter():
    tweets = [
        {"id": 1, "cory_ken": "Motivate"},
        {"id": 2, "kyle_jen": "New Makeup"}
    ]
    return render_template("tweets.html", message="What are they saying on Twitter", tweets=tweets)


@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "TWEET CREATED OK (TODO)",
        "tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")