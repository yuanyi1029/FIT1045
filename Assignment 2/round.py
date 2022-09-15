from __future__ import annotations
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer


class Round:

	def __init__(self, players: list[Player]) -> None:
		self.players = players

	def first_player_update(self, players: list[Player]) -> list[Player]: 

		copied_players = players.copy()

		if self.first_trick_check() is True:
			for playerindex in range(len(players)):	
				for eachcard in players[playerindex].hand:
					if eachcard == Card(Rank.Two, Suit.Clubs):
						reduce_by = playerindex

			# print(players)

			for playerindex in range(len(players)):
				# temporary_object = copied_players[playerindex]
				players[playerindex-reduce_by] = copied_players[playerindex]

			# for playerindex in range(len(players)):
			# 	temporary_object = copied_players[playerindex]
			# 	players[playerindex] = copied_players[playerindex + reduce_by]

			return players


		# if you have two of clubs go first,
			# change the list 
		# if you won the trick
			# change the list

	def first_trick_check(self) -> bool:
		first_trick_status = False
		for eachplayer in self.players:
			for eachcard in eachplayer.hand:
				if eachcard == Card(Rank.Two, Suit.Clubs):
					first_trick_status = True
		return first_trick_status

	def determine_win(self, trick: list[Card], players): #-> player: BasicAIPlayer, points:
		print("in progrress")

	def one_trick(self):
		trick = []
		self.first_player_update(players)
		for eachplayer in players:
			print(eachplayer)
			played_card = eachplayer.play_card(trick, broken_hearts = False)
			trick.append(played_card)

		print(trick)

		# if self.first_trick_check():
		# 	print("its the first trick")
		# else:
		# 	print("not first trick")
		
	def __str__(self):
		return self.one_trick()

if __name__ == "__main__":

	players = [BasicAIPlayer("Player 0"), BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3")]
	players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
	players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades), Card(Rank.Six, Suit.Diamonds)]
	players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Spades)]
	players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds), Card(Rank.King, Suit.Hearts)]

	Round(players)
	r1 = Round(players)
	# print(r1.first_trick_check())
	print(r1.one_trick())
	# print(r1.first_player_check(players))
	
	
