import abc
from cards_definition import *
from card_player import *
import random as rnd

# game definition

class Game(metaclass=abc.ABCMeta):
    """
        Main class to define a game
        Abstract class.
        Each game will herit of this one.
    """

    players: list[CardPlayer]
    cards_set: CardsSet

    def __init__(self, type_of_game:TypeCard, players:list, cards_pack_count:int=1):

        self.players = players
        self.cards_set = CardsSet(type_card = type_of_game, cards_pack_count = cards_pack_count)
        self.distribute()
        
    @property
    def number_of_players(self):
        return len(self.players)

    def _check_distribution(self, number_by_user):
        """
            Check the distribution
            get number of total cards
            throw exception if all rules are not respected:
            total of cards must be greater or equal to the number by users
            multiply by users

            Args:
              - number_by_user

            Returns:
              - None, raise exception if not possible to distribute
        """
        if not(self.number_of_players):
            raise Exception("No players defined")

        if len(self.cards_set.cards) < number_by_user * self.number_of_players:
            raise Exception("So more players for number of cards")

    def distribute(self, number_by_user=-1):
        """Distribution of cards

           Args:
             - number_by_user: if -1 of number by user; then divide package and distribute all

           Returns:
             - None
        """
        self._check_distribution(number_by_user)
        
        if number_by_user < 0:
            number_by_user = len(self.cards_set.cards) // self.number_of_players

        for pl in self.players:
            pl.get_cards(CardSetPlayer(cards = [self.cards_set.cards.pop() for _ in range(number_by_user)], game_type = type(self).__name__))

        return
    
    def __next__(self):
        # stop game if one of player has no card
        if any(map(CardPlayer.has_no_card, self.players)):
            raise StopIteration
        self.next_round()

    @abc.abstractmethod
    def next_round(self):
        pass

    @classmethod
    def rules(cls):
        raise Exception(f"Please, define rules for {cls.__name__} game")

class Tarot(Game):
    """Define Tarot game"""
    def __init__(self, players:list):
        super().__init__(type_of_game = TypeCard.TAROT, players = players)

    def _check_distribution(self, number_by_user):
        """
        Redefine the check distribution for Tarot:
        just need between 3 and 5 players
        """
        print(f"number of players : {self.number_of_players}")
        if not(2 < self.number_of_players < 6):
            raise Exception(f"Not attends numbers of players")		

    def distribute(self, number_by_user:int=-1):
        """
        Distribution has to take 2 rounds:
          - first round, before announce
          - second round after taking announce decision
        """
        pass

    def rules(cls):
        pass

    def next_round(self):
        pass

class Battle(Game):

    @classmethod
    def rules(cls):
        """Define the rules for Battle"""
        pass

    def get_round():
        pass

    def count_round():
        pass

    def next_round(self):
        # check minimum 2 players got cards
        print(sum(map(CardPlayer.has_no_card, self.players)))
        print("Play")
        list(map(lambda pl: pl.play_next(), self.players))


class Pocker(Game):
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

if __name__ == "__main__":
    print("Game test")
    # define 3 players for test
    # create a battle game for test
    players = [CardPlayer(f"Player {i}") for i in range(1, 41)]

    # battle part 2 persons with 54 cards
    battle_2p_54c = Battle(TypeCard.C_54, players[0:2])
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
    for player in players:
        print(player)

    Battle.rules()
    
