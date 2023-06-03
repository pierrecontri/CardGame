# card player
from cards_definition import *

class CardPlayer(object):
    """
    Card Player define the player
    He has a card set
    He define the game he play for
    """
    _cards: CardSetPlayer
    _game_type: str
    
    def __init__(self, name, game_type=None):
        """
        The player name must be defined at the creation
        """
        self.name = name
        self._cards = CardSetPlayer(game_type = game_type)

    def play_next(self):
        pass

    def play_round(self):
        pass
    
    def get_cards(self, cards: CardSetPlayer) -> None:
        self._cards = cards

    @property
    def cards(self) -> list:
        return self._cards

    @property
    def number_of_cards(self):
        return len(self.cards)

    def __str__(self):
        str_cards = ", ".join([str(elem) for elem in self._cards])
        return f"I'm {self.name}, " + \
               (f"I play {self._cards.game_type} and here is my game: [{str_cards}]" \
               if str_cards else "I'm waiting for play")

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
            player.cards.game_type = game_type
        return define_it
