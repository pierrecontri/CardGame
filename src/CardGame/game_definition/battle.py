# Game definition for Battle

from . import base
from ..card_player import CardPlayer
from ..cards_definition import TypeCard
from ..rules import battle as game_rules

class Battle(base.Game):

    def __init__(self, type_of_game:TypeCard, players:list, cards_pack_count:int=1, is_blindly:bool=True):
        super().__init__(type_of_game, players, game_rules, cards_pack_count)
        self._blindly = is_blindly

    @classmethod
    def rules(cls):
        """Define the rules for Battle"""
        pass

    def next_round(self, raise_stop_function=None):
        #print("Play")
        # get players who have cards
        ready_players = [pl for pl in self.players if len(pl.cards)]
        cards_round = game_rules.play_round(players = ready_players,
                                            is_blindly = True)

    def has_next_round(self):
        return game_rules.has_next_round(self.players)

    #def get_winner(self):
    #    return game_rules.get_winner(self.players)

    #def start_game(self):
    #    raise NotImplemented

    #def end_game(self):
    #    raise NotImplemented

    #def start_round(self):
    #    raise NotImplemented

    #def end_round(self):
    #    raise NotImplemented
