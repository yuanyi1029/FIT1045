from __future__ import annotations
from cards import Card, Rank, Suit

class BasicAIPlayer:

	def __init__(self, name: str):
		self.hand = []
		self.round_score = 0 
		self.total_score = 0

	def pass_cards(self) -> Card:
		highest_cards = []
		temporary_list_of_cards = self.hand.copy()

		for i in range (3):
			current_max = max(temporary_list_of_cards)
			highest_cards.append(current_max)
			temporary_list_of_cards.remove(current_max)

		for j in highest_cards:
			print(j)
			
if __name__ == "__main__":
	player = BasicAIPlayer("Test Player 1")
	player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	print(player.pass_cards())
