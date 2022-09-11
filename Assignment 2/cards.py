
from __future__ import annotations # for type hints of a class in itself
from enum import Enum

class Rank(Enum):
	def __lt__(self, other: Rank) -> bool:
		self.Two = 2 
		self.Three = 3
		self.Four = 4
		self.Five = 5
		self.Six = 6
		self.Seven = 7
		self.Eight = 8
		self.Nine = 9 
		self.Ten = 10
		self.Jack = 11
		self.Queen = 12
		self.King = 13 
		self.Ace = 14

		# self.Two = "Two"
		# self.Three = "Three"
		# self.Four = "Four"
		# self.Five = "Five"
		# self.Six = "Six"
		# self.Seven = "Seven"
		# self.Eight = "Eight"
		# self.Nine = "Nine"
		# self.Ten = "Ten"
		# self.Jack = "Jack"
		# self.Queen = "Queen"
		# self.King = "King"
		# self.Ace = "Ace"
		# raise NotImplementedError


class Suit(Enum):
	def __lt__(self, other: Suit) -> bool:
		self.Clubs = 1
		self.Diamonds = 2
		self.Spades = 3
		self.Hearts = 4

		# self.Clubs = "Clubs"
		# self.Diamonds = "Diamonds"
		# self.Spades = "Spades"
		# self.Hearts = "Hearts"
		# raise NotImplementedError


class Card:

	def __init__(self, rank: Rank, suit: Suit) -> None:
		self.rank = Rank
		self.suit = Suit
		# raise NotImplementedError

	# def __repr__(self) -> str:
	# 	raise NotImplementedError

	def __str__(self) -> str:
		print(self.rank + " of " + self.suit)
		raise NotImplementedError

	# def __eq__(self, other: Card) -> bool:
	# 	raise NotImplementedError

	# def __lt__(self, other: Card) -> bool:
	# 	raise NotImplementedError


if __name__ == "__main__":
	card1 = Card(Rank.Two, Suit.Spades)
	card2 = Card(Rank.Ace, Suit.Hearts)

	# print(card1)
	#you can make some local tests here.
	# pass