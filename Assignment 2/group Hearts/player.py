from __future__ import annotations
from cards import Card, Rank, Suit


class Player:

    def __init__(self, name: str) -> None:
        """
        Magic method that initializes the instance variables of the Player class.

        Arguments:
            -name: String of player's name
        """
        self.name = name
        self.hand = []
        self.round_score = 0
        self.total_score = 0

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):
        """
        Method that checks a Card object to see if it is a valid play during a trick and returns a tuple of a boolean
        value which represents the validity of the play and a string which acts as an error message if the card is
        not valid to play.

        Arguments:
            -card: Card object being played
            -trick: List of Card objects in the current trick
            -broken_hearts: Boolean value to represent if hearts have been broken

        Returns a boolean of the validity of play and a string of the error message in tuple type.
        """
        if len(trick) == 0:
            if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):
                return False, 'Player MUST lead the opening trick of the round with the Two of Clubs!'

            elif card.suit == Suit.Hearts and broken_hearts is False:
                return False, 'Player cannot lead with Hearts before hearts have been broken!'

            else:
                return True, 'Valid play'

        # Validation rules for leading the trick:

        # Player has Two of Clubs in hand but does not play it      -> Invalid play
        # Player plays Hearts card but hearts have not been broken  -> Invalid play
        # Every other play                                          -> Valid play

        else:
            able_to_follow_suit = False

            for cards in self.hand:
                if cards.suit == trick[0].suit:
                    able_to_follow_suit = True

            # To determine whether the player has the appropriate cards to be able to follow the suit of the current
            # trick, loop through every card in their hand. The variable able_to_follow_suit will be updated to be
            # True if the suit of a card in the player's hand matches the suit of the current trick.

            if able_to_follow_suit is True:
                if card.suit != trick[0].suit:
                    return False, 'Player still has cards from the suit of the current trick!'

                else:
                    return True, 'Valid play'

            else:
                if trick[0] == Card(Rank.Two, Suit.Clubs):
                    if card.suit == Suit.Hearts or card == Card(Rank.Queen, Suit.Spades):
                        return False, 'Player is not allowed to play Hearts or the Queen of Spades if it is the ' \
                                      'opening trick of the round!'

                    else:
                        return True, 'Valid play'

                else:
                    return True, 'Valid play'

        # Validation rules for following the trick:

        # If player is able to follow the suit of the current trick:
        #     - Player plays a card that does not match the suit of the current trick               -> Invalid play
        #     - Every other play                                                                    -> Valid play

        # If player is not able to follow the suit of the current trick:
        #     - Player plays Hearts or the Queen of Spades during the opening trick of the round    -> Invalid play
        #     - Every other play                                                                    -> Valid play
