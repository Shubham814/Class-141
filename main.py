from flask import Flask,jsonify,request
import csv
from encodings import utf_8

all_movies = []

with open('movies.csv', encoding = "utf_8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    
liked = []
not_liked = []
not_watched = []

app = Flask(__name__)

@app.route("/get-movie")

def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movies", methods = ["POST"])

def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]

    liked.append(movie)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-liked-movies", methods = ["POST"])

def not_liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]

    not_liked.append(movie)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-watched-movies", methods = ["POST"])

def not_watched_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]

    not_watched.append(movie)

    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()