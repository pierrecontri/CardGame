# card player
from cards_definition import *

class CardPlayer(object):
    _cards = []
    """Define a player for game"""
    def __init__(self, name, game_type=None):
        self.name = name
        if game_type:
            self.define_game(game_type)

    def define_game(self, game_type):
        pass

    def play_next(self):
        pass
    
    def get_cards(self, cards: list[Card]):
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        str_cards = ", ".join([str(elem) for elem in self.cards])
        return f"""I'm {self.name} and here is my game:\n[{str_cards}]"""

    @staticmethod
    def give_cards(elem: tuple):
        cards, player = elem
        player.get_cards(cards)
