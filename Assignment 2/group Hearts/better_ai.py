from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player


class BetterAIPlayer(Player):
	"""
	Method that uses the following conditions to provide a more strategic play of card:
		If not leading the trick:

			If able to follow the suit:
				- play a card that is highest in hand but lower than the cards in the trick.

			If trick's opening suit is not Hearts and has Hearts cards in hand but not able to follow the suit:
				- play the highest Hearts card in hand.

		If leading trick:
			If hearts have been broken and has Hearts cards in hand with a rank lower than five:
				- lead with smallest Hearts card in hand.

	Additionally, the method will return the smallest card in the BetterAIPlayer object's hand that is a valid play
	if none of the aforementioned conditions are satisfied.

	Arguments:
		-trick: List of Card objects in the current trick
		-broken_hearts: Boolean value to represent if hearts have been broken
	"""
	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		self.hand.sort()

		card_suit_list = [[], [], [], []]

		for card in self.hand:
			if card.suit == Suit.Clubs:
				card_suit_list[0].append(card)
			elif card.suit == Suit.Diamonds:
				card_suit_list[1].append(card)
			elif card.suit == Suit.Spades:
				card_suit_list[2].append(card)
			elif card.suit == Suit.Hearts:
				card_suit_list[3].append(card)

		# Partitioning cards in hand into suits to make more strategical plays

		if len(trick) != 0 and len(card_suit_list[trick[0].suit.value - 1]) != 0:
			card_suit_list[trick[0].suit.value - 1].reverse()

			# If BetterAIPlayer is not leading the trick and it holds cards in its hand that are the same suit as the
			# trick's opening card. The trick's suit list in card_suit_list will then be reversed to show the highest
			# rank suit first. The key reason is to let the BetterAIPlayer play a card that is the highest in hand
			# but lower than the cards in the trick.

			for card in card_suit_list[trick[0].suit.value - 1]:
				if card.rank < max(trick).rank:
					self.hand.remove(card)
					return card

			# The highest card in the BetterAIPlayer's hand that is less than the highest card (in terms of rank)
			# in the trick may be found by looping through the trick's suit list in card suit list. The card is
			# taken out of the BetterAIPlayer's hand and returned if it is found.

			card = min(card_suit_list[trick[0].suit.value - 1])
			self.hand.remove(card)
			return card

			# The BetterAIPlayer will play the smallest trick card that matches the suit of the trick's opening card
			# if a card that is the highest in hand but lower than the cards in the trick cannot be found.

		elif len(trick) != 0 and len(card_suit_list[trick[0].suit.value - 1]) == 0 and \
				len(card_suit_list[3]) != 0 and broken_hearts and trick[0].suit != Suit.Hearts:

			card = max(card_suit_list[3])
			self.hand.remove(card)
			return card

			# If BetterAIPlayer is not leading the trick and it does not have any cards in its hand that match the
			# trick's opening card, which should not be Hearts, neither does it have any cards in its hand that are
			# the same suit. It will check to see whether it has any Hearts cards in its hand as well as whether
			# hearts have been broken in the game. BetterAIPlayer will play the highest Hearts card it has if all the
			# requirements are met because by doing so it will not take any penalty points.

		elif len(trick) == 0 and broken_hearts \
				and len(card_suit_list[3]) != 0 and min(card_suit_list[3]).rank.value < 5:

			card = min(card_suit_list[3])
			self.hand.remove(card)
			return card

			# If BetterAIPlayer is leading the trick, and hearts have been broken in the game. It will check to see
			# whether it has any Hearts cards in its hand with a rank of less than five. If all conditions are
			# satisfied, BetterAIPlayer will lead the trick with the smallest Hearts card it has so that it may get
			# rid of the Hearts card in its hand and have a low chance of taking the trick and accruing penalty points.

		else:
			for card in self.hand:
				if self.check_valid_play(card, trick, broken_hearts)[0] is True:
					self.hand.remove(card)
					return card

			card = self.hand[0]
			self.hand.pop(0)
			return card

			# If the above special conditions are not met, The BetterAIPlayer is obliged to play the smallest card in
			# hand, which is also the first card in hand, after going through their whole hand and finding no cards
			# that are a valid play. The card is then removed from their hand and returned.

	def pass_cards(self) -> list[Card]:
		"""
		Method that returns the Queen of Spades along with the two highest cards in the BetterAIPlayer object's hand
		if the Queen of Spades is present in the BetterAIPlayer object's hand; if not, it returns the three highest
		cards in the BetterAIPlayer object's hand.

		Returns a list of cards in list type containing Card Objects.
		"""
		self.hand.sort()

		pass_card_list = []

		if Card(Rank.Queen, Suit.Spades) in self.hand:
			pass_card_list.append(Card(Rank.Queen, Suit.Spades))
			self.hand.remove(Card(Rank.Queen, Suit.Spades))
			for i in range(2):
				pass_card_list.append(self.hand[len(self.hand) - 1])
				self.hand.pop()

			# BetterAIPlayer will pass the Queen of Spades with the two highest cards in its hand if it has it in its
			# hand at the beginning of the game. Being in possession of the Queen of Spades throughout the game
			# increases the chance of receiving 13 penalty points.

		else:
			for i in range(3):
				pass_card_list.append(self.hand[len(self.hand) - 1])
				self.hand.pop()

			# If BetterAIPlayer does not have the Queen of Spades in its hand at the start of the game, its hand will
			# be sorted into ascending order, and the highest card is added to the pass_card_list and taken out of
			# the its hand using a for loop (repeating three times).

		pass_card_list.sort()

		return pass_card_list
