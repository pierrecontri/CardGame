# Game definition for Pocker

from . import base
from ..card_player import CardPlayer
from ..cards_definition import TypeCard
from ..rules import pocker as game_rules

class Pocker(base.Game):
    """Traditionnal pocker
       5 cards by persons
       max 3 cards changment by round
       2 round by turn
    """
    number_cards_in_hands = 5
    
    def __init__(self, players: list, cards_pack_count: int=1):
        super().__init__(TypeCard.C_32, players, game_rules, cards_pack_count)
        self.round_number = 0

    def stop_iter():
        raise StopIteration
    
    def distribute(self, raise_stop_function=stop_iter):
        super().distribute(raise_stop_function=raise_stop_function,
                           number_by_user=Pocker.number_cards_in_hands)

    @classmethod
    def rules(cls):
        """Define the rules for Pocker"""
        pass

    def next_round(self, raise_stop_function=stop_iter):
        self.round_number += 1

    def has_next_round(self):
        return self.round_number < 2

    def get_winner(self):
        raise NotImplementedError
