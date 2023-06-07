# Game definition for Tarot

from card_player import *
from . import base
from rules import tarot as tarot_rules

class Tarot(base.Game):
    """Define Tarot game"""
    def __init__(self, players:list):
        super().__init__(type_of_game=TypeCard.TAROT, players=players)

    def _check_distribution(self, number_by_user):
        """
        Redefine the check distribution for Tarot:
        just need between 3 and 5 players
        """
        print(f"number of players : {self.number_of_players}")
        if not(2 < self.number_of_players < 6):
            raise Exception(f"Not attends numbers of players")		

    def stop_iter():
        raise StopIteration

    def distribute(self, raise_stop_function=stop_iter, number_by_user:int=-1):
        """
        Distribution has to take 2 rounds:
          - first round, before announce
          - second round after taking announce decision
        """
        self.next_step()

    def rules(cls):
        pass

    def next_round(self, raise_stop_function=None):
        pass

    def has_next_round(self):
        return False
