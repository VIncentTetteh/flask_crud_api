from flaskcrud import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=True)

    def json(self):
        return {'id': self.id, 'title': self.title, 'year': self.year, 'genre': self.genre}

    def add_movie(title, year, genre):
        new_movie = Movie(title=title, year=year, genre=genre)
        db.session.add(new_movie)
        db.session.commit()

    def get_all_movies(self):
        return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(id):
        return [Movie.json(Movie.query.filter_by(id=id))]

    def update_movie(id, title, year, genre):
        movie_to_update = Movie.query.filter_by(id=id).first()
        movie_to_update.title = title
        movie_to_update.year = year
        movie_to_update.genre = genre
        db.session.commit()

    def delete_movie(id):
        Movie.query.filter_by(id=id).delete()
        db.session.commit()


