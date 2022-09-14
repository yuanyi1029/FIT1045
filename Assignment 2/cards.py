
from __future__ import annotations # for type hints of a class in itself
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

class Suit(Enum):
	Clubs = 1
	Diamonds = 2
	Spades = 3
	Hearts = 4
	def __lt__(self, other: Suit) -> bool:
		return self.value < other.value

class Card:
	def __init__(self, rank: Rank, suit: Suit) -> None:
		self.rank = rank
		self.suit = suit

	def __repr__(self) -> str:
		self.__str__()

	def __str__(self) -> str:
		return f"{self.rank.name} of {self.suit.name}"

	def __eq__(self, other: Card) -> bool:
		return self.rank.value == other.rank.value and self.suit.value == other.suit.value

	def __lt__(self, other: Card) -> bool:
		# return self.suit.value < other.suit.value or self.rank.value < other.rank.value
		return (self.suit.value, self.rank.value) < (other.suit.value, other.rank.value) 


if __name__ == "__main__":
	card1 = Card(Rank.Two, Suit.Clubs)
	card2 = Card(Rank.Ace, Suit.Hearts)
	print(f"{card1}, {card2}")
	print(card2 < card1)
	print(card1 < card2)

	card1 = Card(Rank.Ace, Suit.Clubs)
	card2 = Card(Rank.Two, Suit.Hearts)
	print(f"{card1}, {card2}")
	print(card2 < card1)
	print(card1 < card2)
	pass