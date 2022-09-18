from __future__ import annotations
from cards import Card, Rank, Suit


class Player:
	
	def __init__(self, name: str) -> None:
		raise NotImplementedError

	def __str__(self) -> None:
		raise NotImplementedError

	def __repr__(self) -> None:
		return self.__str__()

	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):
		raise NotImplementedError
