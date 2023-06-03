import abc
from card_player import CardPlayer
from cards_definition import CardsSet, CardSetPlayer, TypeCard

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

    def stop_iter():
        raise StopIteration
    
    def __next__(self, raise_stop_function=stop_iter):
        # stop game if one of player has no card
        if any(map(CardPlayer.has_no_card, self.players)):
            if raise_stop_function:
                raise_stop_function()
            else:
                return

        self.next_round(raise_stop_function)

    @abc.abstractmethod
    def next_round(self, raise_stop_function=None):
        pass

    @classmethod
    def rules(cls):
        raise Exception(f"Please, define rules for {cls.__name__} game")

