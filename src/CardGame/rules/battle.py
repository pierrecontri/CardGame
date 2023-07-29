"""Rules for Battle"""
from card_player import CardPlayer

def has_next_round(players:list) -> bool:
    """
    Check if there is another round
    To run another round, minimum of 2 players contains cards
    """
    number_of_players_available = sum(map(CardPlayer.has_card, players))
    #print(f"sum player with cards: {number_of_players_with_cards}")
    return number_of_players_available > 1

def get_winner(players:list) -> CardPlayer:
    # count card for each players
    # get player with maximum cards
    count_dict = { pl.number_of_cards: pl for pl in players }
    win_idx = max(count_dict)
    return count_dict[win_idx]

def play_round(players, is_blindly=True):
    """
    Each player pull a card on his cards set
    Depends of the Battle_type (blindly or not)
    """
    cards_round: list

    if is_blindly:
        cards_round = [{'player': pl, 'card': pl.cards.pop()} for pl in players]

    else:
        # each player try to put a card on the same color, but more greter than the others players
        cards_round = []

    #print("cards_round")
    #print(cards_round)
    list_sorted = sorted(cards_round, key = lambda x: x['card'], reverse = True)
    # get winner
    winner = list_sorted[0]
    #print("list round sorted")
    #print(list_sorted)
    #print("Winner: " + winner['player'].name)
    #print(winner['card'])
    #get_winner['player'].get_cards
    cards_wins = [kv['card'] for kv in cards_round]
    #print("Cards to winner")
    #print(cards_wins)
    list_sorted[0]['player'].get_cards(cards_wins)
    #exit()
    return (winner, cards_round)


"""
Rules :

- distribution: all cards to players
- start_game: the youngest player start the game
- start_round: each player put a card
- end_round: the player who has the greatest value win
             if execo, all players who has the same value put 2 cards
             the second one is compaired
- end_game: player who has card (the other lost cards)

"""

battle_rules: dict[str, list[object]] = {
        'distribution': None,
        'start_game': None,
        'start_round': None,
        'end_round': None,
        'end_game': None
    }
