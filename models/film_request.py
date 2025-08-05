class FilmRequest():
    def __init__(self, genre: str = "", decade: str = "", rating: str = ""):
        self.genre = genre
        self.decade = decade
        self.rating = rating