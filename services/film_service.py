import os
import requests

class FilmService():
    def __init__(self):
        self.url = "https://api.themoviedb.org/3/discover/movie"
        self.genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-BR"
        self.tmdb_token = os.getenv("TMDB_TOKEN")

    def compose_headers(self):
        headers = { "Authorization": f"Bearer {self.tmdb_token}" }
        return headers
    
    def get_random_film(self, genre: str, decade: int, rating: str, page: int):
        if not decade:
            return requests.get(f"{self.url}?language=pt-BR&vote_average.gte={rating}&with_genres={genre}&vote_count.gte=250&page={page}", headers = self.compose_headers())
        
        return requests.get(f"{self.url}?language=pt-BR&primary_release_date.gte={decade}-01-01&primary_release_date.lte={decade + 9}-12-31&vote_average.gte={rating}&with_genres={genre}&vote_count.gte=250&page={page}", headers = self.compose_headers())

    def get_pages(self, genre: str, decade: int, rating: str):
        if not decade:
            return requests.get(f"{self.url}?language=pt-BR&vote_average.gte={rating}&with_genres={genre}&vote_count.gte=250", headers = self.compose_headers())
        
        return requests.get(f"{self.url}?language=pt-BR&primary_release_date.gte={decade}-01-01&primary_release_date.lte={decade + 9}-12-31&vote_average.gte={rating}&with_genres={genre}&vote_count.gte=250", headers = self.compose_headers())
    
    def get_genres(self):
        return requests.get(self.genre_url, headers=self.compose_headers())