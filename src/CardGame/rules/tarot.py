"""Rules for Tarot"""
from ..card_player import CardPlayer

def get_winner(players:list) -> CardPlayer:
    return players[-1]
