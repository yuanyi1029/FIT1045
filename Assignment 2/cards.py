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

    def __lt__(self, other: Rank) -> bool:
        return self.value < other.value
        # need .value to get the value otherwise will get Class.Name
        # don't need .Suit as self is already Rank


class Suit(Enum):
    Clubs = 1
    Diamonds = 2
    Spades = 3
    Hearts = 4

    def __lt__(self, other: Suit) -> bool:
        return self.value < other.value
        # don't need .Suit as self is already Rank


class Card:

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        suit_art = {
            1: "│  ♣  │",
            2: "│  ♦  │",
            3: "│  ♠  │",
            4: "│  ♥  │"
        }

        rank_art = {
            2: ["┌─────┐", "│2    │", "       ", "│    2│", "└─────┘"],
            3: ["┌─────┐", "│3    │", "       ", "│    3│", "└─────┘"],
            4: ["┌─────┐", "│4    │", "       ", "│    4│", "└─────┘"],
            5: ["┌─────┐", "│5    │", "       ", "│    5│", "└─────┘"],
            6: ["┌─────┐", "│6    │", "       ", "│    6│", "└─────┘"],
            7: ["┌─────┐", "│7    │", "       ", "│    7│", "└─────┘"],
            8: ["┌─────┐", "│8    │", "       ", "│    8│", "└─────┘"],
            9: ["┌─────┐", "│9    │", "       ", "│    9│", "└─────┘"],
            10: ["┌─────┐", "│10   │", "       ", "│   10│", "└─────┘"],
            11: ["┌─────┐", "│J    │", "       ", "│    J│", "└─────┘"],
            12: ["┌─────┐", "│Q    │", "       ", "│    Q│", "└─────┘"],
            13: ["┌─────┐", "│K    │", "       ", "│    K│", "└─────┘"],
            14: ["┌─────┐", "│A    │", "       ", "│    A│", "└─────┘"]
        }

        display_card = ""

        for row in range(len(rank_art[2])):
            display_card += "\n"
            if row != 2:
                display_card += rank_art[self.rank.value][row]

            else:
                display_card += suit_art[self.suit.value]

        return display_card
        # return f'{self.rank.name} of {self.suit.name}'

    def __eq__(self, other: Card) -> bool:
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __lt__(self, other: Card) -> bool:
        return (self.suit, self.rank) < (other.suit, other.rank)
        # compare tuple can compare first then second

    # don't need .suit.value or .rank.value as top class already
    # defined what are them when comparing to inequality signs


if __name__ == "__main__":
    # you can make some local tests here.
    card1 = Card(Rank.Two, Suit.Spades)
    card2 = Card(Rank.Ace, Suit.Hearts)
    print(f"{card1}, {card2}")
    print(card1 > card2)
    pass