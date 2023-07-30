import abc
import importlib
from enum import IntEnum
from ..cards_definition import CardsSet, TypeCard
from ..card_player import CardPlayer

class StateGame(IntEnum):
    INIT = 1
    DISTRIBUTE = 2
    START_GAME = 3
    START_ROUND = 4
    END_ROUND = 5
    END_GAME = 6

class Game(metaclass=abc.ABCMeta):
    """
        Main class to define a game
        Abstract class.
        Each game will herit of this one.
    """

    players: list[CardPlayer]
    cards_set: CardsSet
    dict_orders = {
        StateGame.INIT: lambda x: x.init,
        StateGame.DISTRIBUTE: lambda x: x.distribute,
        StateGame.START_GAME: lambda x: x.start_game,
        StateGame.START_ROUND: lambda x: x.start_round,
        StateGame.END_ROUND: lambda x: x.end_round,
        StateGame.END_GAME: lambda x: x.end_game
    }

    def __init__(self,
                 type_of_game:TypeCard,
                 players:list,
                 rules_mod,
                 cards_pack_count:int=1):

        if rules_mod:
            self.game_rules = rules_mod
            self.game_rules = importlib.import_module(
                                   name=self.game_rules.__name__,
                                   package=self.game_rules.__package__)

        self.players = players
        self._type_of_game = type_of_game
        self._cards_pack_count = cards_pack_count

        self.reset()

    def reset(self):
        # reset players
        for pl in self.players:
            pl.reset()
        # reset the CardsSet
        self.cards_set = CardsSet(type_card = self._type_of_game,
                                  cards_pack_count = self._cards_pack_count)
        self._state_game = StateGame.INIT

    @property
    def number_of_players(self):
        return len(self.players)

    @property
    def winner(self):
        return self.get_winner().name

    def next_step(self):
        self._state_game += 1

    def stop_iter():
        raise StopIteration

    def init(self, raise_stop_function=stop_iter, **kargs):
        #print("Initialisation")
        # next state
        self._state_game += 1

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

    def distribute(self, raise_stop_function=stop_iter, number_by_user=-1):
        """Distribution of cards

           Args:
             - number_by_user: if -1 of number by user; then divide package and distribute all

           Returns:
             - None
        """
        #print("Distribution")
        self._check_distribution(number_by_user)
        
        if number_by_user < 0:
            number_by_user = len(self.cards_set.cards) // self.number_of_players

        for pl in self.players:
            cards = [self.cards_set.cards.pop() for _ in range(number_by_user)]
            pl.get_cards(cards)
            pl.game_type = type(self).__name__

        self.next_step()
        return

    def start_game(self, raise_stop_function=stop_iter, **kargs):
        #print("Start game")
        self.next_step()

    def end_game(self, raise_stop_function=stop_iter, **kargs):
        # start new round if not finished
        if self.has_next_round():
            self._state_game = StateGame.START_ROUND
        # init state if finished
        else:
            #print("End game")
            self._state_game = 0
            raise_stop_function()

    def start_round(self, raise_stop_function=stop_iter, **kargs):
        #print("Start round")
        self.next_round(raise_stop_function)
        self.next_step()

    def end_round(self, raise_stop_function=stop_iter, **kargs):
        self._state_game = StateGame.START_ROUND \
                           if self.has_next_round() \
                           else StateGame.END_GAME
    
    def __next__(self, raise_stop_function=stop_iter, **kargs):
        """
        Based on machine state, execute next order
        """
        #print(f"Machine Status: {self._state_game}")
        # get callable function
        func = Game.dict_orders[self._state_game](self)
        # execute callable
        func(raise_stop_function, **kargs)

    #@abc.abstractmethod
    def get_winner(self):
        return self.game_rules.get_winner(self.players)

    @abc.abstractmethod
    def next_round(self, raise_stop_function=None):
        self.next_step()

    @abc.abstractmethod
    def has_next_round(self) -> bool:
        return False

    @classmethod
    def rules(cls):
        raise Exception(f"Please, define rules for {cls.__name__} game")
