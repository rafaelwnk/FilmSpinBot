from models.genre import Genre

class Film():
    def __init__(self, data, all_genres: list[Genre]):
        self.title = data["title"]
        self.overview = data["overview"]
        self.poster_path = data["poster_path"]
        self.release_date = data["release_date"]
        self.vote_average = data["vote_average"]
        self.genres = [g.name for g in all_genres if g.id in data["genre_ids"]]