from __future__ import annotations
from cards import Card
from player import Player


class BasicAIPlayer(Player):

    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
        """
        Method that returns the smallest card in the BasicAIPlayer object's hand that is a valid play.

        Arguments:
            -trick: List of Card objects in the current trick
            -broken_hearts: Boolean value to represent if hearts have been broken

        Returns a card in Card Object type.
        """
        self.hand.sort()

        count = 0 
        for card in self.hand:
            if self.check_valid_play(card, trick, broken_hearts)[0] is True:
                count += 1
                if count == 2 : 
                    self.hand.remove(card)
                return card

        # Sort the cards in the BasicAIPlayer's hand in ascending order, then loop over the entire hand,
        # checking each card from the smallest to the largest. If a card is a valid play, it is taken out of the
        # BasicAIPlayer's hand and returned.

        card = self.hand[0]
        self.hand.pop(0)
        return card

        # The BasicAIPlayer is obliged to play the smallest card in hand, which is also the first card in hand,
        # after going through their whole hand and finding no cards that are a valid play. The card is then removed
        # from their hand and returned.

    def pass_cards(self) -> list[Card]:
        """
        Method that returns the three highest cards in the BasicAIPlayer object's hand.

        Returns a list of cards in list type containing Card Objects.
        """
        self.hand.sort()

        pass_card_list = []
        for i in range(3):
            pass_card_list.append(self.hand[i])
            self.hand.pop()

        # The BasicAIPlayer's hand is sorted into ascending order, and the highest card is added to the
        # pass_card_list and taken out of the BasicAIPlayer's hand using a for loop (repeating three times).

        pass_card_list.sort()

        return pass_card_list
