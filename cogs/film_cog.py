import random
import discord
from discord import app_commands
from discord.ext import commands
from unidecode import unidecode
from exceptions.genre_not_found_exception import GenreNotFoundException
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
        help_text = """• !f - Gera um filme aleatório baseado nos seguintes filtros: gênero, década e nota mínima. Utilize `.` para ignorar um filtro e considerar todos os valores, ou deixe todos os campos em branco para não aplicar nenhum filtro\n
        Ex: ```!f```
        ```!f Ação 2010 7```
        ```!f . 2010 .```\n
        • !g - Mostra todos os gêneros disponíveis para filtragem\n
        Ex: ```!g```\n
        • !h - Mostra informações sobre os comandos do bot\n
        Ex: ```!h```\n"""
        embed = discord.Embed()
        embed.title = "Help"
        embed.description = help_text
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def f(self, ctx: commands.Context, genre: str = "", decade: str = "", rating: str = ""):
        try:
            if genre == ".":
                genre = ""
            if decade == ".":
                decade = ""
            if rating == ".":
                rating = ""

            genre = unidecode(genre).lower()
            if genre not in self.genres_dict:
                raise GenreNotFoundException(genre)
            
            if decade and not decade.isdigit():
                raise ValueError(f"'{decade}' não é um número inteiro válido para ano.")

            if rating:
                try:
                    float(rating)
                except ValueError:
                    raise ValueError(f"'{rating}' não é um número decimal válido.")
            
            film_request = FilmRequest(self.genres_dict[genre], decade, rating)
            pages = self.service.get_pages(film_request)
            if pages > 500:
                page = random.randint(1, 500)
            else:
                page = random.randint(1, pages)
            
            data = self.service.get_random_film(film_request, page)
            if not data:
                return await ctx.reply("Nenhum filme encontrado.")
            allGenres = self.service.get_genres()
            film = Film(data, allGenres)

            embed = discord.Embed()
            embed.title = f"{film.title} *({film.release_date[:4]}*)"
            embed.description = film.overview
            embed.set_image(url=f"https://image.tmdb.org/t/p/w500/{film.poster_path}")
            embed.set_footer(text=f"{", ".join(film.genres)}  • \u2B50 {round(film.vote_average, 1)}")
            await ctx.reply(embed=embed)
        
        except GenreNotFoundException as e:
            await ctx.reply(e)
        except ValueError as e:
            await ctx.reply(e)
    
    @commands.command()
    async def g(self, ctx: commands.Context):
        allGenres = self.service.get_genres()
        embed = discord.Embed()
        embed.title = "Todos os gêneros"
        embed.description = '\n'.join(f"• {genre.name}" for genre in allGenres)
        embed.set_footer(text="Para gêneros com mais de uma palavra, escreva tudo junto, sem espaços\nEx: Ficçãocientífica, CinemaTV")
        await ctx.reply(embed=embed)