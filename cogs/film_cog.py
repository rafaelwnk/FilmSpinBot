import random
import discord
from discord.ext import commands
from unidecode import unidecode
from exceptions.genre_not_found_exception import GenreNotFoundException
from exceptions.not_enough_films_exception import NotEnoughFilmsException
from models.film import Film
from dtos.film_request import FilmRequest
from services.film_service import FilmService
from views.help_view import HelpView

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
        response = self.service.get_genres()

        if(isinstance(response, str)):
            genres_text = response
        else:
            all_genres = response
            genres_text = '\n'.join(f"• {genre.name}" for genre in all_genres)
            
        view = HelpView(genres_text)
        await ctx.reply(embed=view.pages[0], view=view)
    
    @commands.command()
    async def f(self, ctx: commands.Context, genre: str = "", decade: str = "", rating: str = ""):
        try:
            genre, decade, rating = ("" if x == "." else x for x in (genre, decade, rating))

            genre = unidecode(genre).lower()
            if genre not in self.genres_dict:
                raise GenreNotFoundException(genre)
            
            film_request = FilmRequest(genre=self.genres_dict[genre], decade=decade, rating=rating)
            
            response = self.service.get_random_film(film_request)

            if(isinstance(response, str)):
                return await ctx.reply(response)
            
            film = response

            embed = discord.Embed()
            embed.title = f"{film.title} *({film.release_year}*)"
            embed.description = film.overview
            embed.set_image(url=film.poster_path)
            embed.set_footer(text=f"{", ".join(x.name for x in film.genres)}  • \u2B50 {film.vote_average}")
            await ctx.reply(embed=embed)
        
        except GenreNotFoundException as e:
            await ctx.reply(e)
    
    @commands.command()
    async def g(self, ctx: commands.Context):
        response = self.service.get_genres()

        if(isinstance(response, str)):
            return await ctx.reply(response)

        all_genres = response
        embed = discord.Embed()
        embed.title = "Todos os gêneros"
        embed.description = '\n'.join(f"• {genre.name}" for genre in all_genres)
        embed.set_footer(text="Para gêneros com mais de uma palavra, escreva tudo junto, sem espaços\nEx: Ficçãocientífica, CinemaTV")
        await ctx.reply(embed=embed)

    @commands.command()
    async def s(self, ctx: commands.Context, *, films: str = ""):
        try:
            films_list = [x.strip() for x in films.split(",") if x.strip()]
            if len(films_list) < 2:
                raise NotEnoughFilmsException()
            
            film = random.choice(films_list)
            await ctx.reply(f"O filme sorteado é: {film}")

        except NotEnoughFilmsException as e:
            await ctx.reply(e)