import discord

class HelpView(discord.ui.View):
    def __init__(self, genres_text: str):
        super().__init__(timeout=None)
        self.genres_text = genres_text
        self.page = 0
        self.pages = [
            discord.Embed(title="!f", description="""Gera um filme aleatório com base nos respectivos filtros: gênero, década e nota mínima\n```!f Ação 2010 7```
                          Utilize `.` para ignorar um filtro. No exemplo abaixo, serão considerados todos os gêneros e todas as notas\n```!f . 2010 .```
                          Deixe todos os campos em branco para não aplicar nenhum filtro\n```!f```""").set_author(name="Help"),
            discord.Embed(title="!g", description=f"""Mostra todos os gêneros disponíveis para filtragem\n```!g```
                          **Gêneros:**\n\n{self.genres_text}\n\n*Para gêneros com mais de uma palavra, escreva tudo junto, sem espaços\nEx: Ficçãocientífica, CinemaTV*""").set_author(name="Help"),
            discord.Embed(title="!s", description="""Escolhe um filme aleatório entre os que você passar, separados por ' , '\n```!s Interestelar, Donnie Darko, Scott Pilgrim Contra o Mundo```
                          *Informe pelo menos 2 filmes*""").set_author(name="Help"),
            discord.Embed(title="!h", description="""Mostra informações sobre os comandos do bot\n```!h```""").set_author(name="Help")
        ]
        
        for i, page in enumerate(self.pages):
            page.set_footer(text=f"Página {i+1}/{len(self.pages)}")

    @discord.ui.button(label="<", style=discord.ButtonStyle.gray)
    async def prev(self, interaction: discord.Interaction, button: discord.ui.button):
        self.page = (self.page - 1) % len(self.pages)
        await interaction.response.edit_message(embed=self.pages[self.page], view=self)

    @discord.ui.button(label=">", style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.button):
        self.page = (self.page + 1) % len(self.pages)
        await interaction.response.edit_message(embed=self.pages[self.page], view=self)