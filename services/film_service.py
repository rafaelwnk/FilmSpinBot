import os
import requests
import random
from models.film import Film
from models.film_request import FilmRequest
from models.genre import Genre

class FilmService():
    def __init__(self):
        self.url = "https://api.themoviedb.org/3/discover/movie"
        self.genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-BR"
        self.tmdb_token = os.getenv("TMDB_TOKEN")

    def compose_headers(self):
        headers = { "Authorization": f"Bearer {self.tmdb_token}" }
        return headers
    
    def get_random_film(self, filmRequest: FilmRequest, page: int):
        if not filmRequest.decade:
            response = requests.get(f"{self.url}?language=pt-BR&vote_average.gte={filmRequest.rating}&with_genres={filmRequest.genre}&vote_count.gte=250&page={page}", headers = self.compose_headers())
            data = response.json()
            random_number = random.randint(0, len(data["results"]) - 1)
            return data["results"][random_number]

        response = requests.get(f"{self.url}?language=pt-BR&primary_release_date.gte={filmRequest.decade}-01-01&primary_release_date.lte={filmRequest.decade + 9}-12-31&vote_average.gte={filmRequest.rating}&with_genres={filmRequest.genre}&vote_count.gte=250&page={page}", headers = self.compose_headers())
        data = response.json()
        random_number = random.randint(0, len(data["results"]) - 1)
        return data["results"][random_number]

    def get_pages(self, filmRequest: FilmRequest):
        if not filmRequest.decade:
            response = requests.get(f"{self.url}?language=pt-BR&vote_average.gte={filmRequest.rating}&with_genres={filmRequest.genre}&vote_count.gte=250", headers = self.compose_headers())
            data = response.json()
            return data["total_pages"]

        response = requests.get(f"{self.url}?language=pt-BR&primary_release_date.gte={filmRequest.decade}-01-01&primary_release_date.lte={filmRequest.decade + 9}-12-31&vote_average.gte={filmRequest.rating}&with_genres={filmRequest.genre}&vote_count.gte=250", headers = self.compose_headers())
        data = response.json()
        return data["total_pages"]
    
    def get_genres(self):
        response = requests.get(self.genre_url, headers=self.compose_headers())
        data = response.json()
        return [Genre(genre["id"], genre["name"]) for genre in data["genres"]]