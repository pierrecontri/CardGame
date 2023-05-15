# card player
from cards_definition import *

class CardPlayer(object):
    _cards = []
    _game_type: str
    
    """Define a player for game"""
    def __init__(self, name, game_type=None):
        self.name = name
        self._game_type = game_type
        if game_type:
            self._define_game(game_type)

    def _define_game(self, game_type):
        self._game_type = game_type

    def play_next(self):
        pass
    
    def get_cards(self, cards: list[Card]) -> None:
        self._cards = cards

    @property
    def cards(self) -> list:
        return self._cards

    @property
    def number_of_cards(self):
        return len(self.cards)

    def __str__(self):
        str_cards = ", ".join([str(elem) for elem in self.cards])
        return f"""I'm {self.name}, I play {self._game_type} and here is my game: [{str_cards}]"""

    @classmethod
    def give_cards(cls, elem: tuple) -> None:
        cards, player = elem
        player.get_cards(cards)

    @classmethod
    def has_no_card(cls, player) -> bool:
        return not(player.number_of_cards)
    
    @staticmethod
    def has_card(player) -> bool:
        return not(player.number_of_cards)

    @classmethod
    def define_game(cls, game_type):
        def define_it(player):
            player._define_game(game_type)
        return define_it
