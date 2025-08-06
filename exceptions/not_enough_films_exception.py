class NotEnoughFilmsException(Exception):
    def __init__(self):
        super().__init__("O comando requer no mínimo 2 filmes")