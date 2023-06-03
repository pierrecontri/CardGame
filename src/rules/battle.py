"""Rules for Battle"""
from card_player import CardPlayer

def has_next_round(players):
    """
    Check if there is another round
    To run another round, minimum of 2 players contains cards
    """
    return len(players) - sum(map(CardPlayer.has_no_card, players)) > 1

def play_round(players, is_blindly=True):
    """
    Each player pull a card on his cards set
    Depends of the Battle_type (blindly or not)
    """
    if is_blindly:
        # each player pop a card
        pass
    else:
        # each player try to put a card on the same color, but more greter than the others players
        pass

battle_rules = {
        'round': '',
        'player': ''
    }
