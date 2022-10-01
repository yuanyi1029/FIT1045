from __future__ import annotations
from player import Player
from cards import Card, Rank, Suit

class BasicAIPlayer(Player):

	def __init__(self, name: str):
		super().__init__(name)

	def __str__(self) -> str:
		return self.name

	def __repr__(self) -> str:
		return self.__str__()

	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		# lowest_card = Card(Rank.Ace, Suit.Hearts)

		self.hand.sort()
		for i in self.hand:
			if self.check_valid_play(i, trick, broken_hearts)[0] == True:
				self.hand.remove(i)
				return i

	def pass_cards(self) -> list[Card]:
		highest_cards = []

		for i in range (3):
			current_max = max(self.hand)
			highest_cards.append(current_max)
			self.hand.remove(current_max)
		
		return highest_cards
			

if __name__ == "__main__":
	# Test your function here
	# TASK 2.2 TEST 
	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Two, Suit.Hearts), Card(Rank.Ace, Suit.Spades), Card(Rank.King, Suit.Hearts), Card(Rank.Ten, Suit.Hearts)]
	# trick, broken_hearts = [], False
	# print(player.hand[0])
	# print(player.check_valid_play(player.hand[0], trick, broken_hearts))

	# TASK 2.3 TEST 
	player = BasicAIPlayer("Test Player 1")
	player.hand.append(Card(Rank.Two, Suit.Clubs))
	player.hand.append(Card(Rank.Ace, Suit.Hearts))
	player.hand.append(Card(Rank.King, Suit.Spades))
	player.hand.append(Card(Rank.Ten, Suit.Spades))
	player.hand = [Card(Rank.Queen, Suit.Clubs),Card(Rank.Three, Suit.Hearts), Card(Rank.Eight, Suit.Hearts), Card(Rank.Nine, Suit.Clubs), Card(Rank.Jack, Suit.Spades), Card(Rank.Two, Suit.Diamonds), Card(Rank.Two, Suit.Spades)]
	trick = [Card(Rank.Three, Suit.Diamonds)]
	print(player.play_card(trick, broken_hearts=False))

	# TASK 2.3.1 TEST
	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	# print(player.pass_cards(player.hand))

	# player = BasicAIPlayer("Test Player 1")
	# player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades),]
	# print(player.hand)

	# pass
