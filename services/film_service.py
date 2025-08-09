import os
from typing import Optional
import requests
from dtos.api_response import ApiResponse
from models.film import Film
from dtos.film_request import FilmRequest
from models.genre import Genre

class FilmService():
    def __init__(self):
        self.api_url = os.getenv("API_URL")

    def get_random_film(self, film_request: FilmRequest) -> Film | str:
        response = requests.post(f"{self.api_url}/v1/films", json=film_request.model_dump())
        result = ApiResponse[Optional[Film]].model_validate(response.json())
        if not result.is_success:
            return result.message
        
        return result.data
    
    def get_genres(self) -> list[Genre] | str:
        response = requests.get(f"{self.api_url}/v1/genres")
        result = ApiResponse[Optional[list[Genre]]].model_validate(response.json())
        if not result.is_success:
            return result.message
        
        return result.data