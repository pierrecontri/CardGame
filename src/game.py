
from cards_definition import TypeCard
from card_player import CardPlayer

from game_definition.tarot import Tarot
from game_definition.pocker import Pocker
from game_definition.battle import Battle

__Title__ = """
---..------..------..------.     .------..------..------..------.
|C.--. ||A.--. ||R.--. ||D.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
| :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || (\/) || (\/) |
| :\/: || :\/: || ()() || (__) |'-.-.| :\/: || :\/: || :\/: || :\/: |
| '--'C|| '--'A|| '--'R|| '--'D| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
`------'`------'`------'`------'  '-'`------'`------'`------'`------'

"""

if __name__ == "__main__":
    print(__Title__)
    # define 3 players for test
    # create a battle game for test
    players = [CardPlayer(f"Player {i}") for i in range(1, 41)]

    # battle part 2 persons with 54 cards
    battle_2p_54c = Battle(TypeCard.C_54, players[0:2])
    next(battle_2p_54c)
    next(battle_2p_54c)
    next(battle_2p_54c)
    for _ in range(3000):
        next(battle_2p_54c)
    next(battle_2p_54c)

    # battle part 3 persons with 54 cards
    battle_3p_54c = Battle(TypeCard.C_54, players[2:5])

    # battle part 3 persons with 32 cards
    battle_3p_32c = Battle(TypeCard.C_32, players[5:8])

    # battle part 8 persons with 32 cards
    battle_8p_32c = Battle(TypeCard.C_32, players[8:16])

    # pocker 3 persons with 1 pack
    pocker_3p_1p = Pocker(players[16:20], cards_pack_count = 1)

    # pocker 15 persons with 2 packs // Exception
    # pocker_15p_2p = Pocker(players[20:35], cards_pack_count = 1)

    # pocker 15 persons with 8 packs // Exception
    pocker_10p_4p = Pocker(players[20:30], cards_pack_count = 4)

    # Tarot 6 persons // Exception
    #tarot_6p = Tarot(players[30:36])

    # Tarot 5 persons
    tarot_5p = Tarot(players[30:35])

    # tests
    for player in players[0:2]:
        print(player)

