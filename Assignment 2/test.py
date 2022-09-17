from __future__ import annotations
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer


class Round:

	def __init__(self, players: list[Player]) -> None:
		self.players = players
		self.broken_hearts = False

	# def __str__(self) -> str:
	# 	return self.one_round()

	# def __repr__(self) -> str:
	# 	return self.__str__()


	def one_round(self):
		while len(self.players[0].hand) != 0:
			self.one_trick()
		self.round_end_stats()

	def one_trick(self):
		trick = []

		if self.first_trick_check() is True:
			self.first_turn_players_update(players)

		for eachplayer in players:
			played_card = eachplayer.play_card(trick, self.broken_hearts)
			print(eachplayer.name + " played " + str(played_card))
			if played_card.suit == Suit.Hearts and self.broken_hearts == False:
				self.broken_hearts = True
				print("Hearts have been broken!")
			trick.append(played_card)
		winner = self.winner_check(trick, players)
		if self.first_trick_check() is False: 
			self.other_turn_players_update(players, winner)

	def first_turn_players_update(self, players: list[Player]) -> list[Player]: 

		# print(players)
		copied_players = players.copy()

		for playerindex in range(len(players)):	
			for eachcard in players[playerindex].hand:
				if eachcard == Card(Rank.Two, Suit.Clubs):
					reduce_by = playerindex

		for playerindex in range(len(players)):
			players[playerindex-reduce_by] = copied_players[playerindex]

		return players

	def other_turn_players_update(self, players: list[Player], winner) -> list[Player]:

		copied_players = players.copy()

		for playerindex in range(len(players)):
			if players[playerindex] == winner:
				reduce_by = playerindex

		for playerindex in range(len(players)):
			players[playerindex-reduce_by] = copied_players[playerindex]

		return players

	def first_trick_check(self) -> bool:
		first_trick_status = False
		for eachplayer in self.players:
			for eachcard in eachplayer.hand:
				if eachcard == Card(Rank.Two, Suit.Clubs):
					first_trick_status = True
		return first_trick_status

	def winner_check(self, trick: list[Card], players):
		points = 0 
		winner_index = 0
		winner = None
		main_suit = trick[0].suit
		highest_card = trick[0]

		# determine winner
		for trickindex in range(len(trick)):
			if trick[trickindex].suit == main_suit and trick[trickindex] > highest_card:
				highest_card = trick[trickindex]
				winner_index = trickindex

		winner = players[winner_index]

		# determine points
		for eachcard in trick:
			if eachcard.suit == Suit.Hearts:
				points += 1
			elif eachcard == Card(Rank.Queen, Suit.Spades):
				points += 13
		
		# winner status
		winner.round_score += points
		print(winner.name + " has taken the trick. Points received: " + str(points))
		return winner 

	def round_end_stats(self):
		for player in self.players:
			print(f"{player}'s score: {player.round_score}")
			player.total_score += player.round_score
			player.round_score = 0



if __name__ == "__main__":

	players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4")]
	players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
	players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades), Card(Rank.Six, Suit.Diamonds)]
	players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Spades)]
	players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds), Card(Rank.King, Suit.Hearts)]

	Round(players)
	r1 = Round(players)
	
	# r1.first_turn_players_update(players)
	# r1.other_turn_players_update(players, players[2])

	# print(r1.first_trick_check())
	# print(r1.one_trick())

	# test_players = [BasicAIPlayer("Player 3"), BasicAIPlayer("Player 0"), BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2")]
	# test_trick = [Card(Rank.Queen, Suit.Diamonds),Card(Rank.Jack, Suit.Diamonds), Card(Rank.Four, Suit.Diamonds),Card(Rank.Six, Suit.Diamonds)]
	# test_trick2 = [Card(Rank.Two, Suit.Clubs), Card(Rank.Seven, Suit.Diamonds),Card(Rank.Jack, Suit.Clubs),Card(Rank.Nine, Suit.Clubs)]
	# r1.winner_check(test_trick, test_players)
	# print(r1.first_player_update(players))

	# print(r1.one_trick())
	# print(r1.one_trick())
	# print(r1.one_trick())
	print(r1.one_round())
	# print(test_trick)
	# print(r1.winner_check(test_trick, players))	 
	
	