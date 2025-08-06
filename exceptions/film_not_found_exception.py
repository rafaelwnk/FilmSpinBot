class FilmNotFoundException(Exception):
    def __init__(self):
        super().__init__("Nenhum filme encontrado")