from flask import Flask, jsonify, request
import csv 
all_movies = []

with open("movies.csv", "r", encoding= "utf8") as f:
    csvReader = csv.reader(f)
    data = list(csvReader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch_movies = []

app = Flask(__name__)
@app.route("/get-movie")

def getMovie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route("/liked-movie", methods = ["POST"])

def liked_movie():
    movie = all_movies[0]
    all_movie = all_movies[1:]
    liked_movies.append(movie)
    
    return jsonify({
        "status":"success"
    }),201

@app.route("/not-liked-movie", methods = ["POST"])

def unliked_movie():
    movie = all_movies[0]
    all_movie = all_movies[1:]
    not_liked_movies.append(movie)
    
    return jsonify({
        "status":"success"
    }),201

@app.route("/not-watched-movies", methods = ["POST"])

def did_not_watched_movie():
    movie = all_movies[0]
    all_movie = all_movies[1:]
    did_not_watch_movies.append(movie)
    

    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()