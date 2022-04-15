from flaskcrud import app
from flaskcrud.movies import *
from flask import jsonify, request, Response


@app.route("/movies", methods=['GET'])
def get_movies():
    return jsonify({"Movies": Movie.get_all_movies(self=Movie)})


@app.route("/movies/<int:id>", methods=["GET"])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)


@app.route("/movies/add", methods=["POST"])
def add_movies():
    request_data = request.get_json()
    Movie.add_movie(title=request_data["title"], year=request_data["year"], genre=request_data["genre"])
    response = Response("Movie added", 201, mimetype='application/json')
    return response


@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    request_data = request.get_json()
    Movie.update_movie(id, request_data["title"], request_data["year"], request_data["genre"])
    response = Response("Movies Updated", status=200, mimetype='application/json')
    return response


@app.route("/movies/<int:id>", methods=["DELETE"])
def remove_movie(id):
    Movie.delete_movie(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response
