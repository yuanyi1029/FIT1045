from __future__ import annotations
import random
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from round import Round


class Hearts:

	def __init__(self, target: int, number_of_players: int) -> None:
		self.target = target
		self.number_of_players = number_of_players
		self.players = []

	def game(self, target, number_of_players):

		# create player objects depending on number of players
		for i in range(1, number_of_players+1):
			self.players.append(BasicAIPlayer("Player " + str(i)))
		
		# deal cards to players amd check hands
		self.dealcards(number_of_players, self.players)
		self.playerhandcheck(number_of_players, self.players)

		# r1 = Round(self.players)
		# print(r1.one_round())
		# pass cards to players 
		# print(players)



	def dealcards(self, number_of_players: int, players: list[Player]) -> None:
		full_deck = []
		shuffled_deck = []

		# create deck of 52 cards
		for eachsuit in Suit:
			for eachrank in Rank:
				full_deck.append(Card(eachrank, eachsuit))

		#shuffle deck
		for i in range(len(full_deck)):
			selected = random.choice(full_deck)
			shuffled_deck.append(selected)
			full_deck.remove(selected)

		# remove and deal cards for 3 players or 5 players 
		if number_of_players == 3:
			shuffled_deck.remove(Card(Rank.Two, Suit.Diamonds))
			for i in range(len(shuffled_deck)):
				if i % 3 == 0: 
					players[0].hand.append(shuffled_deck[i])
				elif i % 3 == 1:
					players[1].hand.append(shuffled_deck[i])
				elif i % 3 == 2:
					players[2].hand.append(shuffled_deck[i])

		elif number_of_players == 5:
			shuffled_deck.remove(Card(Rank.Two, Suit.Diamonds))
			shuffled_deck.remove(Card(Rank.Two, Suit.Spades))
			for i in range(len(shuffled_deck)):
				if i % 5 == 0: 
					players[0].hand.append(shuffled_deck[i])
				elif i % 5 == 1:
					players[1].hand.append(shuffled_deck[i])
				elif i % 5 == 2:
					players[2].hand.append(shuffled_deck[i])
				elif i % 5 == 3:
					players[3].hand.append(shuffled_deck[i])
				elif i % 5 == 4:
					players[4].hand.append(shuffled_deck[i])

	def playerhandcheck(self, number_of_players: int, players: list[Player]):
		
		all_valid = True 

		for eachplayer in players:
			player_valid = False 	
			for eachcard in eachplayer.hand:
				if eachcard.suit == Suit.Clubs or eachcard.suit == Suit.Diamonds or (eachcard.suit == Suit.Spades and eachcard != Card(Rank.Queen, Suit.Spades)):
					player_valid = True 

			if player_valid == False:
				all_valid = False

		if all_valid == False:
			# reset all players hand
			for i in players:
				i.hand = []
			# deal cards again
			self.dealcards(number_of_players, self.players)			

	
if __name__ == "__main__":

	# Hearts()
	playercount = 3
	h1 = Hearts(100, playercount)
	h1.game(100, playercount)