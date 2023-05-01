from dataclasses import dataclass
import itertools
from enum import Enum
import random as rnd

class TypeCard(Enum):
    C_32 = 1
    C_54 = 2
    TAROT = 3

@dataclass
class Card:
    """This class define a playing card"""
    color: str
    value: str

    def __str__(self):
        return f"{self.value}{self.color}"

class CardsSet(object):
    """This class is the representation of a clomplete card game.
    By default, there is 32 card, but yes can change it to 54 or Taro game"""

    dict_type_card = {
        TypeCard.C_32: ["A", "K", "Q", "V", "10", "9", "8", "7"],
        TypeCard.C_54: ["K", "Q", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"],
        TypeCard.TAROT: ["K", "Q", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
    }
    
    def __init__(self, type_card:TypeCard=TypeCard.C_32):
        self._type_card = type_card
        self._colors = list(chr(col) for col in range(3, 7, 1))
        self._values = CardsSet.dict_type_card[self._type_card]
        self._asset = "" if self._type_card != TypeCard.TAROT else list(range(1, 21, 1))
        self._elements = list(itertools.product(self._colors, self._values))
        self._cards = [Card(*elem) for elem in self._elements]

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

if __name__ == "__main__":
    game = CardsSet(TypeCard.C_32)
    game_lst = list(game)
    print(game)
    game.shuffle_it()
    print(game.cards)
