from __future__ import annotations
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer

def __init__(self, name: str):
    self.name = name
    self.hand = []
    self.round_score = 0
    self.total_score = 0

def __str__(self) -> str:
    return self.name

def __repr__(self) -> str:
    return self.__str__()

def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
    self.hand.sort()  # sort hand

    if len(trick) == 0:  # if leading

        if broken_hearts:  # if broken hearts return smallest card
            return self.hand[0]

        elif not broken_hearts:  # if not broken hearts return smallest card that is not Hearts

            for i in self.hand:
                if i.suit.value != 4:
                    return i

    else:  # not leading

        for i in self.hand:
            if i.suit.value == trick[0].suit.value:  # check if there is matching suit with lead in hand
                return i

        return self.hand[0]  # if there is no matching suit with lead in hand return smallest card

def pass_cards(self) -> Card:
    pass_cards_list = []

    self.hand.sort()  # sort hand
    self.hand.reverse()  # reverse hand for easier append and pop

    for i in range(3):  # repeat for 3 times
        pass_cards_list.append(self.hand[0])  # append largest card
        self.hand.pop(0)  # pop largest card

    pass_cards_list.sort()  # match with sample output

    return pass_cards_list

def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):
    lead = False

    if len(trick) == 0:
        lead = True

    if lead:
        if Card(Rank.Two, Suit.Clubs) in self.hand and card != Card(Rank.Two, Suit.Clubs):
            # if player has Two of Clubs and do not play it
            return False, 'Player has Two of Clubs and do not play it'
        elif card.suit.value == 4 and not broken_hearts:  # if player plays Hearts and broken_hearts is False
            return False, 'Player plays Hearts and broken_hearts is False'
        else:
            return True

    elif not lead:
        any_card = True
        for i in self.hand:
            if i.suit.value == trick[0].suit.value:  # if hand has card any card suit that is same as trick suit
                any_card = False

        if not any_card:
            if card.suit.value != trick[0].suit.value:  # if player does not play following suit
                return False, 'Player still has cards from the suit of the current trick'
            else:
                return True

        elif any_card:
            if len(trick) == 1:
                if card.suit.value == 4 or card == Card(Rank.Queen, Suit.Spades):
                    # unless this is the first trick of the round, they cannot play Hearts or the Queen of Spades.
                    return False, 'Player cannot play Hearts or Queen of Spades if it is the first trick'
                else:
                    return True
            else:
                return True