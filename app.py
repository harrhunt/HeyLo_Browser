import operator
import os
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users/')
def all_users():
    users = os.listdir("data/people")
    return render_template("users.html", users=users)


@app.route('/users/<user>/')
def this_user(user):
    algs = None
    if user in os.listdir("data/people"):
        algs = [x.split('.')[1] for x in os.listdir(f"data/people/{user}") if "User" in x]
        with open(f"data/people/{user}/{user}.tweets.json", "r") as file:
            tweets = json.load(file)
    return render_template("user.html", user=user, algs=algs, tweets=tweets)


@app.route('/users/<user>/<alg>')
def this_alg(user, alg):
    data = None
    maximum = 0
    if user in os.listdir("data/people"):
        algs = [x.split('.')[1] for x in os.listdir(f"data/people/{user}") if "User" in x]
        if alg in algs:
            with open(f"data/people/{user}/{user}.{alg}.json") as file:
                data = json.load(file)
            maximum = data["interests"][max(data["interests"].items(), key=operator.itemgetter(1))[0]]
    return render_template("data.html", user=user, alg=alg, data=data, maximum=maximum)


if __name__ == '__main__':
    app.run()
