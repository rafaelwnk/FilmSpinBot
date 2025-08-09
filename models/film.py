from pydantic import BaseModel
from models.genre import Genre

class Film(BaseModel):
    id: int
    title: str
    genres: list[Genre]
    overview: str
    poster_path: str
    release_date: str
    vote_average: float