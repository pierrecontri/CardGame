# Game definition for Pocker

from card_player import *
from . import base
from rules import pocker as pocker_rules

class Pocker(base.Game):
    """Traditionnal pocker
       5 cards by persons
       max 3 cards changment by round
       2 round by turn
    """
    number_cards_in_hands = 5
    
    def __init__(self, players: list, cards_pack_count: int=1):
        super().__init__(TypeCard.C_32, players, cards_pack_count)
    
    def distribute(self):
        super().distribute(Pocker.number_cards_in_hands)
        
    @classmethod
    def rules(cls):
        """Define the rules for Pocker"""
        pass

    def next_round(self):
        pass

