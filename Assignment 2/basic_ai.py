from __future__ import annotations
from cards import Card, Rank, Suit

class BasicAIPlayer:

	def __init__(self, name: str):
		self.name = name
		self.hand = []
		self.round_score = 0 
		self.total_score = 0

	def __str__(self) -> str:
		return self.name

	def __repr__(self) -> str:
		return self.__str__()

	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		lowest_card = Card(Rank.Ace, Suit.Hearts)

		for i in self.hand:
			if self.check_valid_play(i, trick, broken_hearts)[0] == True:
				if i < lowest_card: 
					lowest_card = i 

		self.hand.remove(lowest_card)
		return lowest_card

	def pass_cards(self, hand) -> list[Card]:
		highest_cards = []

		for i in range (3):
			current_max = max(hand)
			highest_cards.append(current_max)
			hand.remove(current_max)
		
		return highest_cards
			
	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):

		has_required_suit = False

		leading = False 
		
		if len(trick) == 0:
			leading = True
		

		if leading is True: 											
			for i in self.hand:
				if i.suit == Suit.Clubs or i.suit == Suit.Diamonds or i.suit == Suit.Spades:
					has_required_suit = True	

        # if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):
        #     # if player has Two of Clubs and do not play it
        #     return False, 'Player has Two of Clubs and do not play it'
        # elif card.suit.value == 4 and not broken_hearts:  # if player plays Hearts and broken_hearts is False
        #     return False, 'Player plays Hearts and broken_hearts is False'
        # else:
        #     return True

			if has_required_suit is True:
				# print("same card: " + str(card == Card(Rank.Two , Suit.Clubs)))
				# print("has 2 of clubs: " + str(Card(Rank.Two, Suit.Clubs) in self.hand))
				# print("played two of clubs: " +  str(card == Card(Rank.Two, Suit.Clubs)))

				if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):
					output_tuple = (False, "Player must play Two of Clubs")
				elif card.suit.name == "Hearts" and broken_hearts == False:
					output_tuple = (False, "Player cannot lead with hearts when Hearts are not broken")
				else: 
					output_tuple = (True, "valid play")
			
			elif has_required_suit is False:
				output_tuple = (True, "valid play")

		else:	
			for i in self.hand:
				if trick[0].suit == i.suit:
					has_required_suit = True

			if has_required_suit is True:
				if card.suit != trick[0].suit:
					output_tuple = (False, "Player must Follow Suit")
				else: 
					output_tuple = (True, "valid play")

			elif has_required_suit is False:
				if card == Card(Rank.Queen, Suit.Spades) and trick[0] == Card(Rank.Two, Suit.Clubs):
					output_tuple = (False, "Player cannot play Queen of Spades during the first round")
				else:
					output_tuple = (True, "valid play")		

		# print("leading: " + str(leading))
		# print("has required suit: " + str(has_required_suit))
		# print(output_tuple)
		return output_tuple

if __name__ == "__main__":
	# Test your function here
	# TASK 2.2 TEST 
	player = BasicAIPlayer("Test Player 1")
	player.hand = [Card(Rank.Two, Suit.Hearts), Card(Rank.Ace, Suit.Spades), Card(Rank.King, Suit.Hearts), Card(Rank.Ten, Suit.Hearts)]
	trick, broken_hearts = [], False
	print(player.hand[0])
	print(player.check_valid_play(player.hand[0], trick, broken_hearts))

	# TASK 2.3 TEST 
	# player = BasicAIPlayer("Test Player 1")
	# player.hand.append(Card(Rank.Two, Suit.Clubs))
	# player.hand.append(Card(Rank.Ace, Suit.Hearts))
	# player.hand.append(Card(Rank.King, Suit.Spades))
	# player.hand.append(Card(Rank.Ten, Suit.Spades))
	# trick = []
	# print(player.play_card(trick, broken_hearts=False))

	# TASK 2.3.1 TEST
	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	# print(player.pass_cards(player.hand))

	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	# print(player.hand)

	# pass
