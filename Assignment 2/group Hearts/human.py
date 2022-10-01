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
        print(len("asdfvc"))

        self.hand = [Card(Rank.Queen, Suit.Clubs),Card(Rank.Three, Suit.Hearts), Card(Rank.Eight, Suit.Hearts), Card(Rank.Nine, Suit.Clubs), Card(Rank.Jack, Suit.Spades), Card(Rank.Two, Suit.Diamonds), Card(Rank.Two, Suit.Spades)]
        trick = [Card(Rank.Three, Suit.Diamonds)]
        broken_hearts = False

        # self.play_card(trick, broken_hearts)
        self.pass_cards("test")

        
    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:

        valid = False

        # prints current trick and current hand for user
        print(trick)
        print("Your current hand: ")
        print(self.hand)


        while valid is False:
            card_index_to_play = int_input("Select a card to play: ")

            # if within range of hand, then only check for valid plays
            if self.play_card_validation(card_index_to_play) is True: 
                # if invalid, print the invalid statement 
                if self.check_valid_play(self.hand[card_index_to_play], trick, broken_hearts)[0] is False:
                    print(self.check_valid_play(self.hand[card_index_to_play], trick, broken_hearts)[1])
                # if valid play, valid = True and break loop
                elif self.check_valid_play(self.hand[card_index_to_play], trick, broken_hearts)[0] is True:
                    valid = True
            else:
                print("Not within range of hand!")

        return self.hand[card_index_to_play]
        
    def play_card_validation(self, player_input: int) -> bool:
        valid_input = False
        if player_input >= 0 and player_input < len(self.hand):
            valid_input = True
        return valid_input


    def pass_cards(self, passing_to: str) -> list[Card]:
        valid = False
        cards_to_pass = []
        # prints current hand for user
        print("Your current hand: ")
        print(self.hand)

        # appends their pass selection to a list and return it 
        # WARNING : HARD CODING AT LINE 95
        while valid is False:
            cards_to_pass_index = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
            # only proceed to append the cards if validation is True
            if self.pass_card_validation(cards_to_pass_index) is True:
                valid = True
                for i in range(0,7,3):
                    cards_to_pass.append(self.hand[int(cards_to_pass_index[i])])

        print(f"Passing cards to {passing_to}")

        return cards_to_pass

    def pass_card_validation(self, player_input: str) -> bool:
        valid_input = False
        # WARNING : HARD CODING HERE 
        if len(player_input) >= 6:
            try:
                # try to convert 1st, 4th, 7th character to integer (integer check)
                int(player_input[0]) and int(player_input[3]) and int(player_input[6])
                # check for commas between integers
                if player_input[1] == "," and player_input[4] == ",":
                    # check for spaces between commas
                    if player_input[2] == " " and player_input[5] == " ":
                        valid_input = True 
            except:
                valid_input = False
        
        return valid_input

Human()
