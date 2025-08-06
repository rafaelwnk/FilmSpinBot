class GenreNotFoundException(Exception):
    def __init__(self, genre: str):
        super().__init__(f"Gênero '{genre}' não encontrado")