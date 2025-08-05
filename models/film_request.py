class FilmRequest():
    def __init__(self, genre: str = "", decade: int = None, rating: str = ""):
        self.genre = genre
        self.decade = decade
        self.rating = rating