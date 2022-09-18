from __future__ import annotations
from cards import Card
from player import Player


class Human(Player):
	
	def __init__(self) -> None: 
		raise NotImplementedError
		
	def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
		raise NotImplementedError

	def pass_cards(self) -> Card:
		raise NotImplementedError