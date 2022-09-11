from __future__ import annotations
from cards import Card, Rank, Suit


class BasicAIPlayer:

	def __init__(self, name: str):
		raise NotImplementedError

	def __str__(self) -> str:
		raise NotImplementedError

	def __repr__(self) -> str:
		return self.__str__()

	def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
		raise NotImplementedError

	def pass_cards(self) -> Card:
		raise NotImplementedError

	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):
		raise NotImplementedError


if __name__ == "__main__":
    # Test your function here
    # player = BasicAIPlayer("Test Player 1")
    # player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
    # trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
    # print(player.check_valid_play(player.hand[0], trick, broken_hearts))
    pass
