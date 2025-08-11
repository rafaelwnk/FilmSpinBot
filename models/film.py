from pydantic import BaseModel, Field
from models.genre import Genre

class Film(BaseModel):
    id: int
    title: str
    genres: list[Genre]
    overview: str
    poster_path: str = Field(alias="posterPath")
    release_year: str = Field(alias="releaseYear")
    vote_average: float = Field(alias="voteAverage")