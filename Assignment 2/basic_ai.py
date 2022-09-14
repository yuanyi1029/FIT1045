from __future__ import annotations
from cards import Card, Rank, Suit

class BasicAIPlayer:

	def __init__(self, name: str):
		self.hand = []
		self.round_score = 0 
		self.total_score = 0

	# def __str__(self) -> str:
	# 	raise NotImplementedError

	# def __repr__(self) -> str:
	# 	return self.__str__()

	def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
		raise NotImplementedError

	def pass_cards(self) -> Card:
		raise NotImplementedError

	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):

		if len(trick) == 0: 																	# LEADING
			if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):	# not 1st trick and didnt play 2 of clubs
				output_tuple = (False, "Player must play Two of Clubs")
			elif card.suit.name == "Hearts" and broken_hearts == False:							# broken false, lead with heart
				output_tuple = (False, "Cannot lead with hearts when Hearts are not broken")
			else:
				output_tuple = (True, "valid play")

		else:																					# NOT LEADING		
			has_required_suit = False
			for i in self.hand:
				if trick[0].suit == i.suit:
					has_required_suit = True

			if has_required_suit is True:														# CAN MATCH 	
				if card.suit != trick[0].suit:													# but didnt follow suit
					output_tuple = (False, "Must Follow Suit")
				else: 
					output_tuple = (True, "valid play")

			elif has_required_suit is False:														# CANNOT MATCH 	
				if card == Card(Rank.Queen, Suit.Spades) and trick[0] == Card(Rank.Two, Suit.Clubs):# but play Q spade in 1st round	
					output_tuple = (False, "Cannot play Queen of Spades during the first round")
				else:
					output_tuple = (True, "valid play")		

		return output_tuple

if __name__ == "__main__":
	# Test your function here
	player = BasicAIPlayer("Test Player 1")
	player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
	trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
	# trick, broken_hearts = [], False
	print(player.check_valid_play(player.hand[0], trick, broken_hearts))
	# pass