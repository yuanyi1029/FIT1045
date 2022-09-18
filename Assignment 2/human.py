from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player


def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input
    can also be restricted to a set of integers.

    Arguments:
    - prompt: String representing the message to display for input
    - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)  #
        # if type(player_input) != int: continue
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input

class Human(Player):
	
    def __init__(self) -> None: 
        name = input("Enter a name: ")
        super().__init__(name)

        self.hand = [Card(Rank.Queen, Suit.Clubs),Card(Rank.Three, Suit.Hearts), Card(Rank.Eight, Suit.Hearts), Card(Rank.Nine, Suit.Clubs), Card(Rank.Jack, Suit.Spades), Card(Rank.Two, Suit.Diamonds), Card(Rank.Two, Suit.Spades)]
        trick = [Card(Rank.Three, Suit.Diamonds)]
        broken_hearts = False
        self.play_card(trick, broken_hearts)
        # self.pass_cards("test")

        
    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
        # prints current trick and current hand for user
        print(trick)
        print("Your current hand: ")
        print(self.hand)

        # asks for user to select a card to play (based on the index of their cards in hand)
        card_index_to_play = int_input(input("Select a card to play: "))

        while self.check_valid_play(self.hand[card_index_to_play], trick, broken_hearts)[0] is False:
            # prints the invalid statement if the played card in invalid
            if self.check_valid_play(self.hand[card_index_to_play], trick, broken_hearts)[0] is False:
                print(self.check_valid_play(self.hand[card_index_to_play], trick, broken_hearts)[1])
            # asks for input again 
            card_index_to_play = int(input("Select a card to play: "))
        
        return self.hand[card_index_to_play]

    def pass_cards(self, passing_to: str) -> list[Card]:
        cards_to_pass = []
        # prints current hand for user
        print("Your current hand: ")
        print(self.hand)

        # appends their pass selection to a list and return it 
        # WARNING : HARD CODING AT LINE 46
        cards_to_pass_index = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
        for i in range(0,7,3):
            cards_to_pass.append(self.hand[int(cards_to_pass_index[i])])

        print(f"Passing cards to {passing_to}")

        return cards_to_pass



    def play_card_validation(self, player_input: str) -> bool:
        print("test")

Human()


	# def pass_cards(self) -> list[Card]:
	# 	highest_cards = []

	# 	for i in range (3):
	# 		current_max = max(self.hand)
	# 		highest_cards.append(current_max)
	# 		self.hand.remove(current_max)
		
	# 	return highest_cards