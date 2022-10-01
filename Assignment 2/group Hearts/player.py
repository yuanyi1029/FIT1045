from __future__ import annotations
from cards import Card, Rank, Suit


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.round_score = 0 
        self.total_score = 0

    def __str__(self) -> None:
        return self.name

    def __repr__(self) -> None:
        return self.__str__()

    def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):

        has_required_suit = False
        leading = False 

        # checks if player is leading the trick
        if len(trick) == 0:
            leading = True
            
        if leading is True: 		
            # for leading, check hand for cards other than hearts 								
            for i in self.hand:
                if i.suit == Suit.Clubs or i.suit == Suit.Diamonds or i.suit == Suit.Spades:
                    has_required_suit = True

            # if have other cards than hearts:
            if has_required_suit is True:
                # disallow any other cards except Two of Clubs for first trick
                if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):
                    output_tuple = (False, "Player must play Two of Clubs")
                # disallow playing hearts if hearts not broken yet
                elif card.suit.name == "Hearts" and broken_hearts == False:
                    output_tuple = (False, "Player cannot lead with hearts when Hearts are not broken")
                else: 
                    output_tuple = (True, "valid play")
            
            # if only have heart cards in hand:
            elif has_required_suit is False:
                output_tuple = (True, "valid play")

        else:	
            # for not leading, check hand to see if able to follow suit or not
            for i in self.hand:
                if trick[0].suit == i.suit:
                    has_required_suit = True

            # if hand has required card to follow suit:
            if has_required_suit is True:
                # disallow not following suit 
                if card.suit != trick[0].suit:
                    output_tuple = (False, "Player must Follow Suit")
                else: 
                    output_tuple = (True, "valid play")

            # if dont have required card to follow suit:
            elif has_required_suit is False:
                # disallow queen of spades on the first trick
                if card == Card(Rank.Queen, Suit.Spades) and trick[0] == Card(Rank.Two, Suit.Clubs):
                    output_tuple = (False, "Player cannot play Queen of Spades during the first round")
                else:
                    output_tuple = (True, "valid play")		

        return output_tuple





