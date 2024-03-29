# card player
import random as rnd

class CardPlayer(object):
    """
    Card Player define the player
    He has a card set
    He define the game he play for
    """
    _cards: list
    _game_type: str
    
    def __init__(self, name, game_type=None):
        """
        The player name must be defined at the creation
        """
        self.name = name
        self._cards = []
        self.game_type = game_type

    def reset(self):
        self._cards = []
        self.game_type = None

    def play_next(self):
        pass

    def play_round(self):
        pass

    def get_cards(self, cards: list) -> None:
        #shuffle new cards
        rnd.shuffle(cards)
        self._cards += cards

    @property
    def cards(self) -> list:
        return self._cards

    @property
    def number_of_cards(self):
        return len(self.cards)

    def __str__(self):
        str_cards = ", ".join([str(elem) for elem in self._cards])
        return f"I'm {self.name}, " + \
               (f"I play {self.game_type}" + \
                f" and here is my game: [{str_cards}]" \
               if str_cards else "I'm waiting for play")

    @classmethod
    def give_cards(cls, elem: tuple) -> None:
        cards, player = elem
        player.get_cards(cards)

    def has_card(self) -> bool:
        return bool(self.number_of_cards)
