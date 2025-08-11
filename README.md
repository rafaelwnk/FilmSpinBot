# FilmSpinBot

Bot para Discord do [FilmSpin](https://github.com/rafaelwnk/FilmSpin) que gera filmes aleatórios usando a API do TMDB. Permite filtrar por gênero, década e nota mínima através do comando `!f`. Exibe título, ano de lançamento, gêneros, avaliação, pôster e descrição do filme.

Comandos disponíveis:  
- `!f` : Gera um filme aleatório com filtros opcionais.  
- `!g` : Exibe todos os gêneros disponíveis.  
- `!s` : Sorteia um filme a partir de títulos passados como parâmetro.  
- `!h` : Exibe ajuda com instruções de uso dos comandos.  

## Tecnologias Utilizadas

- Python

## Instalação e Execução
Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos
Antes de iniciar, certifique-se de ter os seguintes itens instalados:

- [Python](https://www.python.org/downloads)

### 1. Clone o repositório:
```bash
git clone https://github.com/rafaelwnk/FilmSpinBot
cd FilmSpinBot
```

### 2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
```
- No Windows:
```bash
venv\Scripts\activate
```
- No Linux/MacOS:
```bash
source venv/bin/activate
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
```bash
BOT_TOKEN=token_do_discord
API_URL=url_filmspin_api
```

### 5. Execute o projeto:
```bash
python main.py
```

## Contribuições

Se você tiver alguma sugestão de melhoria, ideia nova ou perceber algo que pode ser ajustado:

    1.Faça um fork do repositório

    2.Crie uma nova branch: git checkout -b feature

    3.Faça um commit: git commit -m 'feat: new feature'

    4.Faça o push para a branch : git push origin feature

    5.Abra um pull request