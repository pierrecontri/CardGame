# Game definition for Battle

from card_player import *
from . import base
from rules import battle as battle_rules

class Battle(base.Game):

    def __init__(self, type_of_game:TypeCard, players:list, cards_pack_count:int=1, is_blindly:bool=True):
        super().__init__(type_of_game, players, cards_pack_count)
        self._blindly = is_blindly

    @classmethod
    def rules(cls):
        """Define the rules for Battle"""
        pass

    def get_round():
        pass

    def count_round():
        pass

    def next_round(self, raise_stop_function=None):
        # check minimum 2 players got cards
        print(battle_rules.has_next_round(self.players))
        print("Play")
        list(map(lambda pl: pl.play_next(), self.players))


