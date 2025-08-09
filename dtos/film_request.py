from pydantic import BaseModel

class FilmRequest(BaseModel):
    genre: str = ""
    decade: str = ""
    rating: str = ""