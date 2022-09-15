from __future__ import annotations
from cards import Card, Rank, Suit

class BasicAIPlayer:

	def __init__(self, name: str):
		self.hand = []
		self.round_score = 0 
		self.total_score = 0

	# def __str__(self) -> str:
	# 	return self.hand

	# def __repr__(self) -> str:
	# 	return self.__str__()

	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		lowest_card = Card(Rank.Ace, Suit.Hearts)

		for i in self.hand:
			if self.check_valid_play(i, trick, broken_hearts)[0] == True:
				if lowest_card > i: 
					lowest_card = i 
			
		return lowest_card

	def pass_cards(self) -> Card:
		highest_cards = []
		temporary_list_of_cards = self.hand.copy()

		for i in range (3):
			current_max = max(temporary_list_of_cards)
			highest_cards.append(current_max)
			temporary_list_of_cards.remove(current_max)
		
		print(highest_cards)
		# return highest_cards

		# for j in highest_cards:
		# 	print(j)
			
	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):

		if len(trick) == 0: 																	# leading, trick is empty
			if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):	# if not 1st trick and dont play 2 of clubs
				output_tuple = (False, "Player must play Two of Clubs")
			elif card.suit.name == "Hearts" and broken_hearts == False:
				output_tuple = (False, "Cannot lead with hearts when Hearts are not broken")
			else:
				output_tuple = (True, "valid play")

		else:			# not leading			
			has_required_suit = False
			for i in self.hand:
				if trick[0].suit == i.suit:
					has_required_suit = True

			if has_required_suit is True:
				if card.suit != trick[0].suit:
					output_tuple = (False, "Must Follow Suit")
				else: 
					output_tuple = (True, "valid play")

			elif has_required_suit is False:
				if card == Card(Rank.Queen, Suit.Spades) and trick[0] == Card(Rank.Two, Suit.Clubs):
					output_tuple = (False, "Cannot play Queen of Spades during the first round")
				else:
					output_tuple = (True, "valid play")		

		return output_tuple

if __name__ == "__main__":
	# Test your function here
	# TASK 2.2 TEST 
	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
	# trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
	# print(player.check_valid_play(player.hand[0], trick, broken_hearts))

	# TASK 2.3 TEST 
	# player = BasicAIPlayer("Test Player 1")
	# player.hand.append(Card(Rank.Four, Suit.Clubs))
	# player.hand.append(Card(Rank.Ace, Suit.Hearts))
	# player.hand.append(Card(Rank.King, Suit.Spades))
	# player.hand.append(Card(Rank.Ten, Suit.Spades))
	# trick = [Card(Rank.Seven, Suit.Spades)]
	# print(player.play_card(trick, broken_hearts=False))

	# TASK 2.3.1 TEST
	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	# print(player.pass_cards())

	player = BasicAIPlayer("Test Player 1")
	player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	print(player)
	# pass
