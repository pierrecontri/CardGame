from collections import Counter

from cards_definition import TypeCard
from card_player import CardPlayer

from game_definition.tarot import Tarot
from game_definition.pocker import Pocker
from game_definition.battle import Battle

import concurrent.futures as cf
import multiprocessing

__Title__ = """
.------..------..------..------.     .------..------..------..------.
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
    games = []

    # battle part 2 persons with 54 cards
    games.append(Battle(TypeCard.C_54, players[0:2]))

    # battle part 3 persons with 54 cards
    games.append(Battle(TypeCard.C_54, players[2:5]))

    # battle part 3 persons with 32 cards
    games.append(Battle(TypeCard.C_32, players[5:8]))

    # battle part 8 persons with 32 cards
    games.append(Battle(TypeCard.C_32, players[8:16]))

    # pocker 3 persons with 1 pack
    games.append(Pocker(players[16:20], cards_pack_count = 1))

    # pocker 15 persons with 2 packs // Exception
    # pocker_15p_2p = Pocker(players[20:35], cards_pack_count = 1)

    # pocker 15 persons with 8 packs // Exception
    games.append(Pocker(players[20:30], cards_pack_count = 4))

    # Tarot 6 persons // Exception
    #tarot_6p = Tarot(players[30:36])

    # Tarot 5 persons
    games.append(Tarot(players[30:35]))

    # tests
    def test(tmp_game, print_at_end=True):
        while True:
            try:
                next(tmp_game)
            except StopIteration:
                break 
            except Exception as err:
                print("Error unmanaged : " + repr(err))
                break

        if not print_at_end:
            return

        for player in tmp_game.players:
            print(player)

    test(games[1])
    print(games[1].winner)

    list_winners = []
    for _ in range(100):
        games[1].reset()
        test(games[1], False)
        tmp_win = games[1].winner
        list_winners.append(tmp_win)
        print(tmp_win)

    c = Counter(list_winners)
    print(c)

    # with cf.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
    
        # future_to_game = \
            # {executor.submit(test, tmp_game): tmp_game for tmp_game in games}

        # # get results
        # for future in cf.as_completed(future_to_game):
            # data = future_to_game[future]
            # try:
                # data = future.result()
            # except Exception as exc:
                # print('%r generated an exception: %s' % (game, exc))
            # else:
                # print(f"Execution ended for ThreadPool: {future}")
