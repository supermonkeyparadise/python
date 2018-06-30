from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name), self.movies)

    def watched_movies(self):
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))

        return movies_watched

    # [ csv format ]
    # def save_to_file(self):
    #     with open('{}.txt'.format(self.name), 'w') as f:
    #         f.write(self.name + '\n')
    #         for movie in self.movies:
    #             f.write('{},{},{}\n'.format(movie.name, movie.genre, str(movie.watched)))
    #
    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as f:
    #         content = f.readlines()
    #         username = content[0]
    #         movies = []
    #         for line in content[1:]:
    #             movie_data = line.split(',')  # ['name', 'genre', 'watched']
    #             movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == 'True'))
    #
    #         user = cls(username)
    #         user.movies = movies
    #
    #         return user

    # [ Json format ]
    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user
