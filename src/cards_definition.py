from dataclasses import dataclass
import itertools
from enum import Enum
import random as rnd

class TypeCard(Enum):
    C_32 = 1
    C_54 = 2
    TAROT = 3

class CardColor(Enum):
    HEART = 3
    DIAMON = 4
    CLUB = 5
    SPADE = 6

@dataclass
class Card:
    """This class define a playing card"""
    color: str
    value: str

    def __str__(self):
        return f"{self.value}{self.color}"
        
    def __cmp__(self, other):
        return self.value.__cmp__(other.value)
    
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

# class CardSetPlayer(list):
    # """This class is the representation of a card set for each gamer"""

    # def __init__(self, cards=[], game_type=None):
        # super().__init__(cards)
        # self._game_type = game_type

    # def reset():
        # pass

    # @property
    # def game_type(self):
        # return self._game_type
    
    # @game_type.setter
    # def game_type(self, game_type):
        # if game_type != None:
            # self._game_type = game_type
    
class CardsSet(object):
    """
    This class is the representation of a clomplete card game.
    By default, there is 32 card,
    but yes can change it to 54 or Taro game
    """

    dict_values_card = {
        TypeCard.C_32: [
            "A", "K", "Q", "V", "10", "9", "8", "7"
        ],
        TypeCard.C_54: [
            "K", "Q", "V", "10", "9", "8", "7", "6",
            "5", "4", "3", "2", "1"
        ],
        TypeCard.TAROT: [
            "K", "Q", "C", "V", "10", "9", "8", "7",
            "6", "5", "4", "3", "2", "1"
        ]
    }
    
    def __init__(self, type_card:TypeCard=TypeCard.C_32, 
                 shuffle_cards:bool=True, cards_pack_count:int=1):

        self._type_card = type_card
        self._shuffle_cards = shuffle_cards
        self._cards_pack_count = cards_pack_count
        self.reset()

    def reset(self):
        self._colors = list(chr(col) for col in range(3, 7, 1))
        self._values = CardsSet.dict_values_card[self._type_card]
        self._trumps = None \
                       if self._type_card != TypeCard.TAROT \
                       else list(range(1, 21, 1)) # 21 trumps
        elements = itertools.product(self._colors, self._values)
        self._cards = [Card(*elem) for elem in elements] * self._cards_pack_count

        if self._shuffle_cards:
            self.shuffle_it()

    def __iter__(self):
        return iter(self._cards)

    def __repr__(self):
        for elem in self._cards:
            yield elem

    def __str__(self):
        return ", ".join([str(elem) for elem in self._cards])

    def shuffle_it(self):
        rnd.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards

    def __len__(self):
        return len(self.cards)

    @property
    def trumps(self):
        return self._trumps

    def define_trumps(self, color):
        """move the color of cards in a trumps list"""
        pass

    def switch_trumps(self, color):
        """move actual trumps in cards and define another one"""
        pass


if __name__ == "__main__":
    game = CardsSet(TypeCard.C_32)
    game_lst = list(game)
    game.shuffle_it()
    print(game)
