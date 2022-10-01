from __future__ import annotations
from cards import Card
from player import Player


# 3 Changes for BetterAI Player
# 1. If there is a heart in the trick, don't play highest card, play a smaller heart card to get rid of heart.
# 2. If first trick, 
# 3. 

# Strategy source : 
# https://mobilityware.helpshift.com/hc/en/42-hearts-card-game/faq/2629-advanced-strategy/?p=web

class BetterAIPlayer(Player):
    	
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
        raise NotImplementedError

    def pass_cards(self) -> list[Card]:
        raise NotImplementedError


	# def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
	# 	# lowest_card = Card(Rank.Ace, Suit.Hearts)

	# 	self.hand.sort()
	# 	for i in self.hand:
	# 		if self.check_valid_play(i, trick, broken_hearts)[0] == True:
	# 			self.hand.remove(i)
	# 			return i

	# def pass_cards(self) -> list[Card]:
	# 	highest_cards = []

	# 	for i in range (3):
	# 		current_max = max(self.hand)
	# 		highest_cards.append(current_max)
	# 		self.hand.remove(current_max)
		
	# 	return highest_cards