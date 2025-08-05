import random
import discord
from discord import app_commands
from discord.ext import commands
from unidecode import unidecode
from models.film import Film
from models.film_request import FilmRequest
from services.film_service import FilmService

class FilmCog(commands.Cog):
    def __init__(self, service: FilmService):
        self.service = service
        self.genres_dict = {
            "": "",
            "acao": "28",
            "aventura": "12",
            "animacao": "16",
            "comedia": "35",
            "crime": "80",
            "documentario": "99",
            "drama": "18",
            "familia": "10751",
            "fantasia": "14",
            "historia": "36",
            "terror": "27",
            "musica": "10402",
            "misterio": "9648",
            "romance": "10749",
            "ficcaocientifica": "878",
            "cinematv": "10770",
            "thriller": "53",
            "guerra": "10752",
            "faroeste": "37"
        }

    @commands.command()
    async def h(self, ctx: commands.Context):
        help_text = """• /film ou !f - Gera um filme aleatório baseado nos seguintes filtros: genre (gênero), decade (década) e rating (nota mínima)\n
        Ex: ```/film Ação 2010 7```\n
        ```!f Ação 2010 7```\n
        • /genres ou !g - Mostra todos os gêneros disponíveis para filtragem\n
        Ex:  ```/genres ```\n
        ```!g```\n
        • /help ou !h - Mostra informações sobre os comandos do bot\n
        Ex:  ```/help ```\n
        ```!h```\n"""
        embed = discord.Embed()
        embed.title = "Help"
        embed.description = help_text
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def f(self, ctx: commands.Context, genre: str = "", decade: int = None, rating: str = ""):
        genre = unidecode(genre).lower()
        film_request = FilmRequest(self.genres_dict[genre], decade, rating)
        pages = self.service.get_pages(film_request)
        if pages > 500:
            page = random.randint(1, 500)
        else:
            page = random.randint(1, pages)
        
        data = self.service.get_random_film(film_request, page)
        allGenres = self.service.get_genres()
        film = Film(data, allGenres)

        embed = discord.Embed()
        embed.title = f"{film.title} *({film.release_date[:4]}*)"
        embed.description = film.overview
        embed.set_image(url=f"https://image.tmdb.org/t/p/w500/{film.poster_path}")
        embed.set_footer(text=", ".join(film.genres))
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def g(self, ctx: commands.Context):
        allGenres = self.service.get_genres()
        embed = discord.Embed()
        embed.title = "Todos os gêneros"
        embed.description = '\n'.join(f"• {genre.name}" for genre in allGenres)
        embed.set_footer(text="Para gêneros com mais de uma palavra, escreva tudo junto, sem espaços\nEx: Ficçãocientífica, CinemaTV")
        await ctx.reply(embed=embed)

    @app_commands.command(description="Mostra informações sobre os comandos do bot")
    async def help(self, interact: discord.Interaction):
        help_text = """• /film ou !f - Gera um filme aleatório baseado nos seguintes filtros: genre (gênero), decade (década) e rating (nota mínima)\n
        Ex: ```/film Ação 2010 7```\n
        ```!f Ação 2010 7```\n
        • /genres ou !g - Mostra todos os gêneros disponíveis para filtragem\n
        Ex:  ```/genres ```\n
        ```!g```\n
        • /help ou !h - Mostra informações sobre os comandos do bot\n
        Ex:  ```/help ```\n
        ```!h```\n"""
        embed = discord.Embed()
        embed.title = "Help"
        embed.description = help_text
        await interact.response.send_message(embed=embed)

    @app_commands.command(description="Gera um filme aleatório com base nos filtros")
    @app_commands.describe(genre = "Gênero do filme (deixe em branco para buscar em todos os gêneros)", decade = "Ano inicial da década (deixe em branco para buscar em todas as décadas)", rating = "Nota mínima do filme (deixe em branco para buscar filmes de todas as notas)")
    async def film(self, interact: discord.Interaction, genre: str = "", decade: int = None, rating: str = ""):
        genre = unidecode(genre).replace(" ", "").lower()
        film_request = FilmRequest(self.genres_dict[genre], decade, rating)
        pages = self.service.get_pages(film_request)
        if pages > 500:
            page = random.randint(1, 500)
        else:
            page = random.randint(1, pages)
        
        data = self.service.get_random_film(film_request, page)
        allGenres = self.service.get_genres()
        film = Film(data, allGenres)

        embed = discord.Embed()
        embed.title = f"{film.title} *({film.release_date[:4]}*)"
        embed.description = film.overview
        embed.set_image(url=f"https://image.tmdb.org/t/p/w500/{film.poster_path}")
        embed.set_footer(text=", ".join(film.genres))
        await interact.response.send_message(embed=embed)

    @app_commands.command(description="Veja todos os gêneros disponíveis")
    async def genres(self, interact: discord.Interaction):
        allGenres = self.service.get_genres()
        embed = discord.Embed()
        embed.title = "Todos os gêneros"
        embed.description = '\n'.join(f"• {genre.name}" for genre in allGenres)
        await interact.response.send_message(embed=embed)