import abc
from cards_definition import *
from card_player import *
import random as rnd

# game definition

class Game(metaclass=abc.ABCMeta):
    """Main class to define a game"""
    players: list[CardPlayer]
    cards_set: CardsSet

    @property
    def number_of_players(self):
        return len(self.players)

    def check_distribution(self, number_by_user):
        if not(self.number_of_players):
            raise Exception("No players defined")
        # get number of total cards
        # throw exception if all rules are not respected
        if len(self.cards_set.cards) < number_by_user * self.number_of_players:
            raise Exception("So more players for number of cards")

    @abc.abstractmethod
    def distribute(self, number_by_user=-1):
        # distribution of cards
        # if -1 cards divide package and distribute all
        self.check_distribution(number_by_user)
        
        # random shuffle
        self.cards_set.shuffle_it()
        


class TarotGame(Game):
    """Define Tarot game"""
    def __init__(self):
        pass

    def __setattr__():
        """Check number of players in game, ..."""
        pass

    def rules(cls):
        pass

class Battle(Game):
    def __init__(self, players):
        self.cards_set = CardsSet(TypeCard.C_54)
        self.players = players
        self.distribute()

    def distribute(self):
        super().distribute(len(self.players))
        
        # divide by number of players if number_by_user is not defined
        # distribute
        dist_packs = [self.cards_set.cards[i::self.number_of_players] for i in range(self.number_of_players)]
        lst_tty = list(zip(dist_packs, self.players))
        list(map(CardPlayer.give_cards, lst_tty))

    @staticmethod
    def rules():
        """Define the rules for Battle"""
        pass

if __name__ == "__main__":
    print("Game test")
    # define 3 players for test
    # create a battle game for test
    players = [CardPlayer("P1"), CardPlayer("P2"), CardPlayer("P3")]
    battle = Battle(players[0:2])
    for player in players:
        print(player)
