from __future__ import annotations  # for type hints of a class in itself
from enum import Enum


class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    # Each Enum element in Rank is assigned a distinct integer value according to the deck's ordering.

    def __lt__(self, other: Rank) -> bool:
        return self.value < other.value

    # To compare the size of values of two Enum elements in Rank, the magic method __lt__ is used.


class Suit(Enum):
    Clubs = 1
    Diamonds = 2
    Spades = 3
    Hearts = 4

    # Each Enum element in Suit is assigned a distinct integer value according to the deck's ordering.

    def __lt__(self, other: Suit) -> bool:
        return self.value < other.value

    # To compare the size of values of two Enum elements in Suit, the magic method __lt__ is used.


class Card:

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'{self.rank.name} of {self.suit.name}'

    # When print() is used, the magic method __str__ is implemented to output "Name of Rank of Name of Suit".

    def __eq__(self, other: Card) -> bool:
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __lt__(self, other: Card) -> bool:
        return (self.suit, self.rank) < (other.suit, other.rank)

    # The sizes of two Cards may be found to be comparable by comparing the values in terms of Suit first,
    # followed by Rank, in the magic function __eq__. This is done by placing the suit and rank of a Card in a tuple.
